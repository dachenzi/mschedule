from .cm import  ConnectionManager
from .conf import MASTER_URL

class Master:
    def __init__(self, url=MASTER_URL):
        self.server = ConnectionManager(url)


    def start(self):
        self.server.start()


    def shutdown(self):
        self.server.shutdown()