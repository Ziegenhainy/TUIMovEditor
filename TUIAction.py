class TUIAction:
    def __init__(self, action_func, action_args: tuple=(), seconds=0, nanoseconds=0):
        self.seconds = seconds
        self.nanoseconds = nanoseconds
        self.action_func = action_func
        self.action_args = action_args