from logging.handlers import RotatingFileHandler
import logging
import time

logger = logging.getLogger('hello')
logger.setLevel(logging.INFO)

handler = RotatingFileHandler('/Users/lixin/test.log', maxBytes=10 * 1024,backupCount=5, encoding='UTF-8')
handler.setLevel(logging.INFO)
formatter = logging.Formatter(fmt='%(asctime)s [ %(levelname)s %(funcName)s ] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#################

for i in range(100000):
    time.sleep(0.01)
    logger.error('msg = {}'.format(i))
