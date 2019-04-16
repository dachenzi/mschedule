import logging
from logging.handlers import TimedRotatingFileHandler

import time

logger = logging.getLogger('hello')
logger.setLevel(logging.INFO)

handler = TimedRotatingFileHandler('/Users/lixin/text.log',when='S',interval=10,backupCount=5,encoding='UTF-8')
handler.setLevel(logging.INFO)

formatter = logging.Formatter(fmt='%(asctime)s [ %(levelname)s %(funcName)s ] %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)


for i in range(1000000):
    time.sleep(1)
    logger.error('msg = {}'.format(i))