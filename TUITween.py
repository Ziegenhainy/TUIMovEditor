from tuitime import *

class TUITween:
    def __init__(self, end_val, time: TUITime, frame_handler, ease_func):
        self.end_val: int = end_val
        self.time: TUITime = time
        self.frame_handler: callable = frame_handler 
        self.ease_func: callable = ease_func