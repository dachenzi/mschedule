import logging
from logging.handlers import RotatingFileHandler
from conf import settings

# 按照大小来滚动日志
def getlogger(mod_name, filename: str, level=logging.INFO, propagate=False,
              maxBytes=10 * 1024 * 10, backupCount=5):
    logger = logging.getLogger(mod_name)
    logger.setLevel(level)
    logger.propagate = propagate

    # handler = logging.FileHandler(filename, encoding='UTF-8')
    handler = RotatingFileHandler(filename, maxBytes=maxBytes, backupCount=backupCount, encoding='UTF-8')
    handler.setLevel(level)
    formatter = logging.Formatter(fmt='%(asctime)s [ %(levelname)s %(funcName)s ] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
