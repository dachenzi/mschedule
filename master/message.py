from .storage import Storage


class Message:
    """
    RPC 暴露给客户端的接口
    """

    def __init__(self):
        self.store = Storage()

    def reg(self, msg: dict):
        text = 'reg message: {}'.format(msg)
        print(text)
        ts = msg['timestamp']
        # Agent(msg['id'],msg['hostname'],msg['ips'])
        self.store.reg(msg['id'], msg['hostname'], msg['ips'])
        # TODO 时间校验
        # raise Exception ,可以自定义一个异常类
        return text

    def heartbeat(self, msg: dict):
        # 告诉master，client还活着
        text = 'heartbeat message: {}'.format(msg)

        self.store.heartbeat(msg['id'], msg['timestamp'])
        return text

    def add_task(self, task: dict):
        id = self.store.add_task(task)
        return id

    def pull_task(self, agent_id):
        # task_id, script, timeout = self.store.get_task_by_agentid(agent_id)
        # return task_id, script, timeout
        return self.store.get_task_by_agentid(agent_id)

    def result(self,msg):
        self.store.result(msg)
        return 'ack result'

    def agents(self):
        return self.store.get_agents()  #