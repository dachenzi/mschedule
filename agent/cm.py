import zerorpc
from .conf import MASTER_URL
from threading import Event
from utils import getlogger
from .message import Message
logger = getlogger(__name__)

class ConnectionMessage:
    def __init__(self):
        self.client = zerorpc.Client()
        self.event = Event()
        self.message = Message()

    def start(self):
        while not self.event.wait(1):
            try:
                # 注册信息
                self.client.connect(MASTER_URL)
                self.client.reg(self.message.register())  # reg是server端的

                # 心跳信息
                while True:
                    self.client.heartbeat(self.message.heartbeat())

            except Exception as e:
                logger.error(e)

    def shutdown(self):
        pass