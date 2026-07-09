from .MovableObject import *
from ..utils import *

class TextObject(MovableObject):
    def render(self, canvas: list[list[str]]):
        for i, c in enumerate(self.text):
            if self.y < 0: break
            if self.y >= len(canvas): break
            if self.x+i < 0: continue
            if self.x+i >= len(canvas[0]): break
            canvas[self.y][self.x+i] = c

    def write_tween(self, text, time: TUITime(), ease_func: callable = linear_ease):
        return TUITween(
            len(text), time, lambda step: self.append_text(text[step]), ease_func
        )

    def append_text(self, text):
        self.text += text

    def __init__(self, x, y, text):
        super().__init__(x,y)
        self.text = text