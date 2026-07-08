from TUIObject import *

class TextObject(TUIObject):
    def render(self, canvas: list[list[str]]):
        for i, c in enumerate(self.text):
            if self.y < 0: break
            if self.y >= len(canvas): break
            if self.x+i < 0: continue
            if self.x+i >= len(canvas[0]): break
            canvas[self.y][self.x+i] = c

    def move(self, x=0, y=0):
        self.x += x
        self.y += y

    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text