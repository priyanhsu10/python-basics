import logging
from logging.handlers import RotatingFileHandler
# timedRotatingHandler ,jsonlogger is there for loging as josn data need to search ()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))

logger.addHandler(handler)

for i in range(10000):
    logger.info(f'this is info message {i}')
