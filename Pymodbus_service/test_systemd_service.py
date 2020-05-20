import time
import logging
import sys

# Mock modbus query every 60 seconds
modbus_query_interval = 10
# last_modbus = 0

# Mock Solcast query every 20 seconds
solcast_interval = 10
# last_solcast = 0


def do_work(last_modbus_param, last_solcast_param):
    # global last_modbus, last_solcast

    now = time.time()

    if now - last_modbus_param > modbus_query_interval:
        last_modbus_param = now
        # Mock read RTU etc
        logging.info('Mock reading signals from RTU and saving signals, last_modbus is ... {}'.format(last_modbus_param))
        time.sleep(3)

    if now - last_solcast_param > solcast_interval:
        last_solcast_param = now
        # Mock send payload to Solcast
        logging.info('Mock sending signal payload to Solcast, last_solcast is ... {}'.format(last_solcast_param))
        time.sleep(1)

    return last_modbus_param, last_solcast_param

def main():

    last_modbus = 0
    last_solcast = 0

    while True:
        # do_work()
        new_values = do_work(last_modbus, last_solcast)
        last_modbus, last_solcast = new_values
        time.sleep(1)


if __name__ == "__main__":

    logging.basicConfig(
    # filename='/Users/stevetriplett/temp/pymodbus_master.log',
    stream=sys.stdout,
    # level=logging.DEBUG,
    level=logging.INFO,
    format='%(asctime)s %(message)s', datefmt='%d/%m/%Y %H:%M:%S'
    )
    logging.debug(' ')# Blank line at start of run
    logging.info(' ')# Blank line at start of run

    main()
