


class State:
    WAITING = 'WAITING'
    RUNNING = 'RUNNING'
    SUCCESS = 'SUCCESS'
    FAILED = 'FAILED'


class AgentState(State):
    pass


class TaskState(State):
    pass