from .cm import ConnectionMaster
from .conf import MASTER_URL


class Agent(object):
    def __init__(self, url=MASTER_URL):
        self.url = url
        self.cm = ConnectionMaster(url)

    def start(self):
        self.cm.start()  # 阻塞

    def shutdown(self):
        self.cm.shutdown()


