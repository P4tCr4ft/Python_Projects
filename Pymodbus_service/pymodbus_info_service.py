# Steve Triplett
# HARDsoftware
# March 2020

# Infolite Python MODBUS service

from pymodbus.client.sync import ModbusTcpClient

import pymodbus_info_library as lib
import pymodbus_info_config as conf

import time
import logging
import sys


def main(last_rtu_param, last_solcast_param):
    """
    main function
    """
    # Create connection client object for connection to RTU
    # client = ModbusTcpClient(host=conf.rtu_ip, port=conf.rtu_port)

    # Time value used to determine when to run particular functions
    now = time.time()

    # Create readings dictionary for use throughout program
    readings_from_rtu = {}

    # Major time-based event reading the RTU, building up readings_from_rtu,
    # used for most other app activity
    if now - last_rtu_param > rtu_query_interval:
        last_rtu_param = now

        # Iterate through RTUs in config, call build function for each signal type dictionary in config,
        # building up read RTU results after each iteration
        try:
            # if client.connect():  # connection is OK

            for key, value in conf.rtus.items():

                client = ModbusTcpClient(host=value['rtu_ip'], port=value['rtu_port'])
                rtu_slave_id = value['rtu_slave_id']
                if client.connect():  # connection is OK
                    for data_type, data_dict in value.items():
                        if data_type in ['rtu_ip', 'rtu_port', 'rtu_slave_id']:
                            continue
                        lib.build_consecutive_addresses(
                            data_type, data_dict, readings_from_rtu,
                            lib.map_rtu_functions[data_type][0], getattr(client, lib.map_rtu_functions[data_type][1]),
                            lib.map_rtu_functions[data_type][2], lib.map_rtu_functions[data_type][3],
                            rtu_slave_id,
                        )

        except Exception as e:
            logger.exception('A connection exception occurred - {}'.format(e))

        finally:
            client.close()
            logger.debug('Client connection to RTU has been closed')

        # Mock read RTU etc
        # logger.info('Mock reading signals from RTU and saving signals, last_rtu is ... {}'.format(last_rtu_param))
        # time.sleep(3)

    if not conf.rtu_test_only:
        # call read MySQL scada_signals function, for production mode
        from_my_sql_signals = lib.read_mysql_scada_signals()

    # Compare control fb tags with db and write new values to RTU if necessary, for production mode
        lib.handle_control_tags(client, readings_from_rtu, from_my_sql_signals)

    if now - last_solcast_param > solcast_interval:
        last_solcast_param = now
        # Mock send payload to Solcast
        logger.info('Mock sending signal payload to Solcast, last_solcast is ... {}'.format(last_solcast_param))
        time.sleep(1)

    return last_rtu_param, last_solcast_param


if __name__ == "__main__":

    # # Setup top level logger for main program
    log_format_long = logging.Formatter(
        '%(levelname) -5s %(name)s %(module)s %(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S'
    )
    log_format = logging.Formatter('%(levelname) -5s %(module)s %(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
    std_hand = logging.StreamHandler(sys.stdout)
    std_hand.setLevel(logging.DEBUG)
    std_hand.setFormatter(log_format)
    error_hand = logging.StreamHandler(sys.stderr)
    error_hand.setLevel(logging.ERROR)
    error_hand.setFormatter(log_format_long)

    # Call root logger and configure for use throughout application
    logger = logging.getLogger()
    logger.setLevel(conf.logging_level)
    logger.addHandler(std_hand)
    logger.addHandler(error_hand)

    # Mock RTU query every 60 seconds
    rtu_query_interval = 10
    last_rtu = 0

    # Mock Solcast query every 20 seconds
    solcast_interval = 10
    last_solcast = 0

    # Test for RTU test mode or production mode
    if conf.rtu_test_only:
        logger.debug('Program is in RTU test mode only')
        new_values = main(last_rtu, last_solcast)
    else:
        # Setup loop for running as a service
        while True:
            print("Need this line so debugger stops on first go on breakpoint below - dumb ...")
            new_values = main(last_rtu, last_solcast)
            last_rtu, last_solcast = new_values
            time.sleep(1)
