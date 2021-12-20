import logging
logger = logging.getLogger(__name__)

# create the handlers
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

# level and format
stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formater = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_h.setFormatter(formater)
file_h.setFormatter(formater)

logger.addHandler(stream_h)
logger.addHandler(file_h)


logger.warning('this is warning')
logger.error('this is error')
