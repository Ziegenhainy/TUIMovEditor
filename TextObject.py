from TUIObject import *
from tuitime import *
from TUITween import *
from easefuncs import *

class TextObject(TUIObject):
    def render(self, canvas: list[list[str]]):
        for i, c in enumerate(self.text):
            if self.y < 0: break
            if self.y >= len(canvas): break
            if self.x+i < 0: continue
            if self.x+i >= len(canvas[0]): break
            canvas[self.y][self.x+i] = c

    def move_tween(self, x=0, y=0, time: TUITime = TUITime(), ease_func = linear_ease):
        return TUITween(
            x, time, lambda step: self.move(x=1), ease_func
        ), TUITween(
            y, time, lambda step: self.move(y=1), ease_func
        )

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text