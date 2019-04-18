import zerorpc
from .message import Message
from .conf import MASTER_URL


class ConnectionManager:

    def __init__(self, url=MASTER_URL):
        self.server = zerorpc.Server(Message())
        self.url = url

    def start(self):
        self.server.bind(self.url)
        self.server.run()

    def shutdown(self):
        self.server.close()
