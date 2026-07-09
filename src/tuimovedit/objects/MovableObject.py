from .TUIObject import TUIObject
from ..utils import *
from ..TUITween import *

class MovableObject(TUIObject):
    def move_tween(self, x=0, y=0, time: TUITime = TUITime(), ease_func = linear_ease):
        return (
            self.move_x_tween(x,time,ease_func),
            self.move_y_tween(y,time,ease_func)
        )

    def move_x_tween(self, x=0, time: TUITime = TUITime(), ease_func = linear_ease): 
        return TUITween(
            abs(x), time, lambda step: self.move(x=1 if x>=0 else -1), ease_func
        )

    def move_y_tween(self, y=0, time: TUITime = TUITime(), ease_func = linear_ease):
        return TUITween(
            abs(y), time, lambda step: self.move(y=1 if y>=0 else -1), ease_func
        )

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def __init__(self, x, y):
        self.x = x
        self.y = y