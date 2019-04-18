import datetime
from common import agent


class Agent:
    """
    客户端注册后的信息需要封装，提供一个信息存储的类，数据存储在类的实例中
    """

    def __init__(self, id, hostname, ips):
        # 可以加一个时间校验，或者在message中接收到注册信息的时候就做一个校验。这里用服务器的时间
        self.reg_time = datetime.datetime.now()
        self.id = id
        self.hostname = hostname
        self.ips = ips
        self.state = agent.WAITING
        self.outputs = {}
        self.lastupdatetime = None

    def __repr__(self):
        return '<Agent {} {} {}>'.format(self.id, self.hostname, self.ips)
