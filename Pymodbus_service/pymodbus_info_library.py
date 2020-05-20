# Steve Triplett
# HARDsoftware
# March 2020

# Infolite Python MODBUS library of functions


from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.payload import BinaryPayloadBuilder

import logging
import pymodbus.pdu
import pymodbus_info_config as conf

if not conf.rtu_test_only:
    from sqlalchemy import create_engine, text
    from sqlalchemy.orm import sessionmaker
    from preprod_scada_readings_table import Scada_Readings, Scada_Signals, Base

# Can just use root logger here (which has had handlers attached in main program)
# instead of defining a new logger using this module (eg, logger = logging.getLogger('__name__')
# Can do this by calling root logger again here for use in this module as follows;
logger = logging.getLogger()


def build_consecutive_addresses(
        data_type, type_dict, readings_from_rtu, local_read_rtu_function,
        pymodbus_read_rtu_function, regs_per_signal, type_msg_string, rtu_slave_id
        ):
    """
    Function which reads modbus signal info from config file, builds a list of consecutive addresses and passes
    it to RTU read function, and continues to do so until there are no signals left in config. The RTU read function reads
    RTU and stores results in dictionary, to be used to send to db, etc.
    """
    signal_list = []
    total_number_signals = len(type_dict)

    try:
        if total_number_signals == 0:
            raise ModbusAddressError('There are no {}s in config'.format(type_msg_string))
        # Setup comparison between consecutive signals in config
        get_next = get_next_address(type_dict)
        start_signal = get_next.__next__()
        signal_list.append(start_signal)
        get_comparison = get_next_address(type_dict)
        get_comparison.__next__()
        for idx in range(total_number_signals):
            try:
                comparison_candidate = get_comparison.__next__()
                # If address is consecutive to starting address, add it to signal_list
                if data_type in ['coil_control_tags', 'coils', 'discrete_inputs']:
                    if start_signal[1] == comparison_candidate[1] - regs_per_signal:
                        signal_list.append(comparison_candidate)
                        start_signal = get_next.__next__()
                        continue
                else:
                    if start_signal[1][0] == comparison_candidate[1][0] - regs_per_signal:
                        signal_list.append(comparison_candidate)
                        start_signal = get_next.__next__()
                        continue
            except Exception as e:
                if isinstance(e, StopIteration):
                    logger.debug('1st StopIteration - No more consecutive {} candidates'.format(type_msg_string))
                else:
                    logger.exception('Exception occurred processing {} - {}'.format(type_msg_string, e))
            # Signal_list is ready for RTU reading
            local_read_rtu_function(
                signal_list, readings_from_rtu, pymodbus_read_rtu_function,
                regs_per_signal, type_msg_string, rtu_slave_id
                )
            logger.info('No more consecutive {} candidates'.format(type_msg_string))
            try:
                start_signal = get_next.__next__()
                signal_list = [start_signal]
                continue
            except Exception as e:
                if isinstance(e, StopIteration):
                    logger.debug('2nd StopIteration - No more consecutive {} candidates'.format(type_msg_string))
                else:
                    logger.exception('Exception occurred processing {} - {}'.format(type_msg_string, e))
    except ModbusAddressError as e:
        logger.info('Exception occurred processing {} - {}'.format(type_msg_string, e.message))
    except Exception as e:
        logger.exception('Exception occurred processing {} - {}'.format(type_msg_string, e))


def get_next_address(dict):
    """
    Function which reads a single signal from config
    """
    for key, value in dict.items():
        yield key, value


def read_rtu_floats(
        signal_list, readings_from_rtu, pymodbus_read_rtu_function,
        regs_per_signal, type_msg_string, rtu_slave_id
        ):
    """
    Function taking a list of signals generated from the config file, reading corresponding addresses in RTU
    and storing the results in-place in readings_from_rtu, which will be sent to db
    """
    try:
        number_hr_regs = int(len(signal_list)*2)
        first_hr_reg = signal_list[0][1][0]
        result = pymodbus_read_rtu_function(first_hr_reg, number_hr_regs, unit=rtu_slave_id)
        if isinstance(result, pymodbus.pdu.ExceptionResponse):
            raise ModbusAddressError(result)
        first_part = 0
        second_part = 1
        for signal in signal_list:
            decoder = BinaryPayloadDecoder.fromRegisters(
                [result.registers[first_part], result.registers[second_part]],
                byteorder=Endian.Big, wordorder=Endian.Big
                )
            hr = decoder.decode_32bit_float()
            logger.info("'{}' (addr {}) is ... {}".format(signal[0], signal[1][0], hr))
            readings_from_rtu[signal[0]] = hr
            if hr < signal[1][1]: logger.info('    WARNING: Reading out of range - LOW')
            if hr > signal[1][2]: logger.info('    WARNING: Reading out of range - HIGH')
            first_part += 2
            second_part += 2
    except ModbusAddressError as e:
        logger.info('Exception occurred reading {} Floats in RTU - {}'.format(type_msg_string, e.message))
    except Exception as e:
        logger.exception('Exception occurred reading {} Floats in RTU - {}'.format(type_msg_string, e))


def read_rtu_integers(
        signal_list, readings_from_rtu, pymodbus_read_rtu_function,
        regs_per_signal, type_msg_string, rtu_slave_id
        ):
    """
    Function taking a list of signals generated from the config file, reading corresponding addresses in RTU
    and storing the results in-place in readings_from_rtu. Handles scaled U16Bit and U32Bit integers.
    """
    try:
        number_hr_regs = int(len(signal_list)*regs_per_signal)
        first_hr_reg = signal_list[0][1][0]
        result = pymodbus_read_rtu_function(first_hr_reg, number_hr_regs, unit=rtu_slave_id)
        if isinstance(result, pymodbus.pdu.ExceptionResponse):
            raise ModbusAddressError(result)
        if regs_per_signal > 1:
            first_part = 0
            second_part = 1
            for signal in signal_list:
                decoder = BinaryPayloadDecoder.fromRegisters(
                    [result.registers[first_part], result.registers[second_part]],
                    byteorder=Endian.Little, wordorder=Endian.Little
                    )
                if signal[1][1] < 0:
                    hr = decoder.decode_32bit_int()
                else:
                    hr = decoder.decode_32bit_uint()
                # If scaling exists apply it
                if len(signal[1]) == 3:
                    readings_from_rtu[signal[0]] = hr
                    logger.info("'{}' (addr {}) is ... {}".format(signal[0], signal[1][0], hr))
                elif len(signal[1]) == 4:
                    # apply scale
                    logger.info(
                        "'{}' (addr {}) is ... {} (Raw value {})".format(signal[0], signal[1][0], hr / signal[1][3], hr)
                        )
                    readings_from_rtu[signal[0]] = hr / signal[1][3]
                else:
                    logger.info('Check signal data in config - too many values ({})'.format(len(signal)))
                    raise IndexError
                if readings_from_rtu[signal[0]] < signal[1][1]: logger.info('    WARNING: Reading out of range - LOW')
                if readings_from_rtu[signal[0]] > signal[1][2]: logger.info('    WARNING: Reading out of range - HIGH')
                first_part += 2
                second_part += 2
        else:
            for idx, signal in enumerate(signal_list):
                decoder = BinaryPayloadDecoder.fromRegisters(
                    [result.registers[idx]], byteorder=Endian.Big, wordorder=Endian.Big
                    )
                if signal[1][1] < 0:
                    hr = decoder.decode_16bit_int()
                else:
                    hr = decoder.decode_16bit_uint()
                # If scaling exists apply it
                if len(signal[1]) == 3:
                    readings_from_rtu[signal[0]] = hr
                    logger.info("'{}' (addr {}) is ... {}".format(signal[0], signal[1][0], hr))
                elif len(signal[1]) == 4:
                    # apply scale
                    logger.info(
                        "'{}' (addr {}) is ... {} (Raw value {})".format(signal[0], signal[1][0], hr / signal[1][3], hr)
                        )
                    readings_from_rtu[signal[0]] = hr / signal[1][3]
                else:
                    logger.info('Check signal data in config - too many values ({})'.format(len(signal)))
                    raise IndexError
                if readings_from_rtu[signal[0]] < signal[1][1]: logger.info('    WARNING: Reading out of range - LOW')
                if readings_from_rtu[signal[0]] > signal[1][2]: logger.info('    WARNING: Reading out of range - HIGH')
    except ModbusAddressError as e:
        logger.info('Exception occurred reading {} Integers in RTU - {}'.format(type_msg_string, e.message))
    except Exception as e:
        logger.exception('Exception occurred reading {} Integers in RTU - {}'.format(type_msg_string, e))


def read_rtu_coils_di(
        signal_list, readings_from_rtu, pymodbus_read_rtu_function,
        regs_per_signal, type_msg_string, rtu_slave_id
        ):
    """
    Function takes list of COIL and/or DISCRETE INPUT signals from config and reads corersponding addresses in RTU
     and stores results, for sending to db, etc.
    """
    try:
        number_regs = len(signal_list)
        first_reg = signal_list[0][1]
        result = pymodbus_read_rtu_function(first_reg, number_regs, unit=rtu_slave_id)
        if isinstance(result, pymodbus.pdu.ExceptionResponse):
            raise ModbusAddressError(result)
        for idx in range(number_regs):
            logger.info("'{}' (addr {}) is ... {}".format(signal_list[idx][0], signal_list[idx][1], result.bits[idx]))
            readings_from_rtu[signal_list[idx][0]] = result.bits[idx]
    except ModbusAddressError as e:
        logger.info('Exception occurred reading {} in RTU - {}'.format(type_msg_string, e.message))
    except Exception as e:
        logger.exception('Exception occurred reading {} in RTU - {}'.format(type_msg_string, e))


def read_mysql_scada_signals():
    """
    Get latest readings_from_rtu populated in MySQL Infolite database
    """
    try:
        engine = create_engine('mysql+pymysql://parser:B3@9ood^^4N@10.2.28.22/infolite')

        # Bind the engine to the Base class for use in the db_session instance
        Base.metadata.bind = engine
        db_session = sessionmaker(bind=engine)
        session = db_session()
        # Query all readings_from_rtu from scada_signals table
        query_string = "SELECT * FROM scada_signals ORDER BY signal_at DESC LIMIT 1"
        signals = session.query(Scada_Signals).from_statement(text(query_string)).one()
        logger.debug('Latest readings_from_rtu from scada_signals MySQL table are {}'.format(signals.__dict__))
        return signals
    except Exception as e:
        logger.info('An Exception occurred reading MySQL database - {}'.format(e))
    finally:
        session.close()
        logger.debug('MySQL session has been closed')


def handle_control_tags(client, readings_from_rtu, mysql_signals, hr_control_tag_floats=True):
    """
    Function to test control tag feedback values read from RTU against corresponding in MySQL scada_signals,
    and if necessary, write new values to RTU.
    If hr_control_tag_floats=False then HR control tags will be written to as 16Bit integers
    """
    new_coil_control_tags = {}
    new_hr_control_tags = {}

    try:
        # use config control_tags to read corresponding COILS out of readings_from_rtu
        for key in conf.coils_control_tags.keys():
            fb_reading = key + '_fb'
            if readings_from_rtu[fb_reading] == bool(mysql_signals.__dict__[key]):
                logger.debug(
                    "Control tag fb '{}' value {} is equal to scada_signals {}"
                    .format(fb_reading, readings_from_rtu[fb_reading], bool(mysql_signals.__dict__[key])))
            else:
                new_coil_control_tags[key] = mysql_signals.__dict__[key]
                logger.debug(
                    "Control tag fb '{}' value {} does not match new value in scada_signals {}, listed for over-write"
                    .format(fb_reading, readings_from_rtu[fb_reading], bool(mysql_signals.__dict__[key])))
        # use config control_tags to read corresponding HR out of readings_from_rtu
        for key in conf.holding_registers_control_tags.keys():
            fb_reading = key + '_fb'
            if readings_from_rtu[fb_reading] == mysql_signals.__dict__[key]:
                logger.debug(
                    "Control tag fb '{}' value {} is equal to scada_signals {}"
                    .format(fb_reading, readings_from_rtu[fb_reading], bool(mysql_signals.__dict__[key])))
            else:
                new_hr_control_tags[key] = mysql_signals.__dict__[key]
                logger.debug(
                    "Control tag fb '{}' value {} does not match new value in scada_signals {}, listed for over-write"
                    .format(fb_reading, readings_from_rtu[fb_reading], bool(mysql_signals.__dict__[key])))
    except Exception as e:
        logger.exception('Exception occurred comparing control tags  - {}'.format(e))

    # If necessary, write new control tag values from scada_signals to RTU
    try:
        if new_coil_control_tags:
            for key, value in new_coil_control_tags.items():
                client.write_coil(conf.coils_control_tags[key], value)
                logger.info("New control tag value {} for '{}' written to RTU".format(value, key))
    except Exception as e:
        logger.exception('Exception occurred writing new COIL control tags to RTU - {}'.format(e))
    try:
        if new_hr_control_tags:
            builder = BinaryPayloadBuilder(byteorder=Endian.Big, wordorder=Endian.Big)
            if hr_control_tag_floats:
                for key, value in new_hr_control_tags.items():
                    builder.add_32bit_float(value)
                    payload = builder.build()
                    client.write_registers(conf.holding_registers_control_tags[key][0], payload, skip_encode=True)
                    logger.info("New control tag value {} for '{}' written to RTU".format(value, key))
            else:
                for key, value in new_hr_control_tags.items():
                    builder.add_16bit_uint(value)
                    payload = builder.build()
                    client.write_registers(conf.holding_registers_control_tags[key][0], payload, skip_encode=True)
                    logger.info("New control tag value {} for '{}' written to RTU".format(value, key))

                # Pretty sure will never have to write 32Bit integers, but should be able to if need be.
                # BinaryPayloadBuilder would need little endian if 32Bit read is anything to go by.

        # Note: if we had consecutive addresses we could write all at once, instead of building payload
        #       individually and writing for each signal individually. But seeing as it's only max of
        #       8 signals at present, it's safer to just write them individually, so address order doesn't matter

    except Exception as e:
        logger.exception('Exception occurred writing new HR control tags to RTU - {}'.format(e))


# Mapping for data type to required pymodbus and local read RTU functions
map_rtu_functions = {
    'coil_control_tags': (read_rtu_coils_di, 'read_coils', 1, 'COIL CONTROL TAGS'),
    'hr_16bit_float_control_tags': (read_rtu_floats, 'read_holding_registers', 1, 'HOLDING REGISTER 16BIT FLOAT CONTROL TAGS'),
    'hr_32bit_float_control_tags': (read_rtu_floats, 'read_holding_registers', 2, 'HOLDING REGISTER 32BIT FLOAT CONTROL TAGS'),
    'hr_16bit_int_control_tags': (read_rtu_integers, 'read_holding_registers', 1, 'HOLDING REGISTER 16BIT INT CONTROL TAGS'),
    'hr_32bit_int_control_tags': (read_rtu_integers, 'read_holding_registers', 2, 'HOLDING REGISTER 32BIT INT CONTROL TAGS'),
    'coils': (read_rtu_coils_di, 'read_coils', 1, 'COIL'),
    'discrete_inputs': (read_rtu_coils_di, 'read_discrete_inputs', 1, 'DISCRETE INPUT'),
    'hr_16bit_floats': (read_rtu_floats, 'read_holding_registers', 1, 'HOLDING REGISTER 16BIT FLOATS'),
    'hr_32bit_floats': (read_rtu_floats, 'read_holding_registers', 2, 'HOLDING REGISTER 32BIT FLOATS'),
    'hr_16bit_ints': (read_rtu_integers, 'read_holding_registers', 1, 'HOLDING REGISTER 16BIT INTS'),
    'hr_32bit_ints': (read_rtu_integers, 'read_holding_registers', 2, 'HOLDING REGISTER 32BIT INTS'),
    'ir_16bit_floats': (read_rtu_floats, 'read_input_registers', 1, 'INPUT REGISTER 16BIT FLOATS'),
    'ir_32bit_floats': (read_rtu_floats, 'read_input_registers', 2, 'INPUT REGISTER 32BIT FLOATS'),
    'ir_16bit_ints': (read_rtu_integers, 'read_input_registers', 1, 'INPUT REGISTER 16BIT INTS'),
    'ir_32bit_ints': (read_rtu_integers, 'read_input_registers', 2, 'INPUT REGISTER 32BIT INTS'),
}


# User defined Exception definition
class ModbusAddressError(Exception):
    def __init__(self, message):
        self.message = message
