from tuitime import *

class TUIAction:
    def __init__(self, action_func, action_args: tuple=(), time: TUITime = TUITime()):
        self.time        = time
        self.action_func = action_func
        self.action_args = action_args