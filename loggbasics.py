import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%( )s -%(name)s -%(levelname)s - %(message)s', datefmt='%m/%d/%Y %H:%M:%S')
logging.debug('this  is debug message')
logging.info('this is info message')
logging.warning('this is worning message')
logging.error('this is error message')
logging.critical('this is critical message')
