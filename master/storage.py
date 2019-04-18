import uuid
from .agent import Agent
from .task import Task
import common


class Storage:
    """
    负责agents/tasks的存储，必要时实现持久化
    """

    def __init__(self):
        self.agents = {}  # 注册的agent的字典
        # TODO 以agent来分类task任务(思考，是否可以）
        self.tasks = {}  # 任务的字典

    def reg(self, id, hostname, ips):
        if id not in self.agents.keys():
            self.agents[id] = Agent(id, hostname, ips)
        else:
            agent = self.agents[id]
            agent.ips = ips
            agent.hostname = hostname

    def heartbeat(self, id, timestamp):  # heartbeat: ip, timestamp
        # TODO 心跳包更新agent时间
        pass

    def add_task(self, task: dict):
        id = uuid.uuid4().hex

        # TODO 判断key是否存在
        t = Task(id, **task)
        t.targets = {agent_id: self.agents[agent_id] for agent_id in t.targets}

        # 加入任务列表
        self.tasks[t.id] = t
        return t.id

    def iter_tasks(self, state={common.task.WAITING, common.task.RUNNING}):
        # for task in self.tasks.values():
        #     if task.state in state:
        #         yield task
        yield from (task for task in self.tasks.values() if task.state in state)

    def get_task_by_agentid(self, agent_id):
        for task in self.iter_tasks():
            if agent_id in task.targets.keys():  # 此agent是可以执行任务的
                # TODO 异常判断
                agent = self.agents[agent_id]
                if task.id not in agent.outputs:
                    agent.outputs[task.id] = None

                    task.state = common.task.RUNNING
                    agent.state = common.agent.RUNNING

                    return task.id, task.script, task.timeout

    def result(self, msg: dict):
        agent_id = msg['id']
        agent = self.agents[agent_id]
        # TODO 异常捕获
        agent.outputs[msg['task_id']] = {
            'code': msg['code'],
            'output': msg['output']
        }
        self.state = common.agent.WAITING

    def get_agents(self):
        return {agent.id: agent.hostname for agent in self.agents.values()}
