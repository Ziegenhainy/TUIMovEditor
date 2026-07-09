from .MovableObject import *
from ..utils import *

class TextObject(MovableObject):
    def render(self, canvas: list[list[str]]):
        for text_y, line in enumerate(self.text.split("\n")):
            if self.y+text_y < 0: continue
            if self.y+text_y >= len(canvas): break
            for text_x, c in enumerate(line):
                if self.x+text_x < 0: continue
                if self.x+text_x >= len(canvas[0]): break
                canvas[self.y+text_y][self.x+text_x] = c

    def write_tween(self, text, time: TUITime(), ease_func: callable = linear_ease):
        return TUITween(
            len(text), time, lambda step: self.append_text(text[step]), ease_func
        )

    def append_text(self, text):
        self.text += text

    def __init__(self, x, y, text):
        super().__init__(x,y)
        self.text = text