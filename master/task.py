from common import task


class Task:
    """
    任务封装类，任务就是类的一个个实例
    """

    def __init__(self, id, script, timeout, parallel=1, fail_count=0, fail_rate=0, targets=None):
        self.id = id
        self.script = script  # 命令,shell脚本
        self.timeout = timeout
        if targets == None:
            self.targets = {}  # 此任务派发给几个agent
        else:
            self.targets = targets

        self.state = task.WAITING
        self.parallel = parallel  # 最大并发
        self.fail_count = fail_count  # 最多任务失败的个数，用于
        self.fail_rate = fail_rate  # 失败率
        self.targets_count = len(self.targets)

    def __repr__(self):
        return '<Task {} {}>'.format(self.id, self.state)
