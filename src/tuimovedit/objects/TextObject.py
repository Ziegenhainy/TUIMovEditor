from .MovableObject import *

class TextObject(MovableObject):
    def render(self, canvas: list[list[str]]):
        for i, c in enumerate(self.text):
            if self.y < 0: break
            if self.y >= len(canvas): break
            if self.x+i < 0: continue
            if self.x+i >= len(canvas[0]): break
            canvas[self.y][self.x+i] = c

    def __init__(self, x, y, text):
        super().__init__(x,y)
        self.text = text