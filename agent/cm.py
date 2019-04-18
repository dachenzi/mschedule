import zerorpc
from threading import Event, Thread
from utils import getlogger
from .message import Message
from .executor import Executor
import common

logger = getlogger(__name__, '/Users/lixin/agent.cm.log')


class ConnectionMaster:
    def __init__(self, url):
        self.client = zerorpc.Client()
        self.event = Event()
        self.message = Message()
        self.url = url
        self.exec = Executor()
        self.state = common.task.WAITING

    def __exec(self, task):
        # TODO 如果做base64就需要做base64解码
        task_id, script, timeout = task
        code, text = self.exec.run(script, timeout)  # code,text
        # self.client.result(task_id, result)    # zerorpc不能跨线程

        self.__result = task_id, code, text

        self.state = common.task.SUCCESS if code == 0 else common.task.FAILED

    def start(self, interval=5):
        while not self.event.wait(1):
            try:
                # 注册信息
                self.client.connect(self.url)
                self.client.reg(self.message.register())  # reg是server端的

                # 心跳信息
                while not self.event.wait(interval):
                    # logger.error('心跳消息已发送')
                    self.client.heartbeat(self.message.heartbeat())

                    if self.state in {common.task.SUCCESS, common.task.FAILED}:
                        ack = self.client.result(self.message.result(*self.__result))

                        logger.info('{}'.format(self.__result))
                        self.__result = None
                        self.state = common.task.WAITING

                    if self.state == common.task.WAITING:
                        task = self.client.pull_task(self.message.id)
                        if task:
                            self.state = common.task.RUNNING
                            Thread(target=self.__exec, args=(task,)).start()

            except Exception as e:
                logger.error(e)

    def shutdown(self):
        self.event.set()
        self.client.close()
