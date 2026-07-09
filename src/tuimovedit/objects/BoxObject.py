from .MovableObject import *

class BoxObject(MovableObject):
    """boxChars may have null character (\\0) to indicate an empty space"""

    def render(self, canvas: list[list[str]]):
        box_char_y = 0
        for y_box in range(self.height):
            if y_box == self.height-1: box_char_y = 2
            elif y_box == 1: box_char_y = 1

            if y_box+self.y < 0: continue
            if y_box+self.y >= len(canvas): break

            box_char_x = 0
            for x_box in range(self.width):
                if x_box == self.width-1: box_char_x = 2
                elif x_box == 1: box_char_x = 1

                if x_box+self.x < 0: continue
                if x_box+self.x >= len(canvas[0]): break
                
                box_char = self.box_chars[box_char_y][box_char_x]
                if box_char == "\0": continue

                canvas[y_box+self.y][x_box+self.x] = box_char

    def size(self, x, y):
        self.width = max(self.width+x,0)
        self.height = max(self.height+y,0)

    def __init__(self, x=0, y=0, width=3, height=3, box_chars = (
        "╔═╗",
        "║ ║",
        "╚═╝")):
        super().__init__(x,y)
        self.width = width
        self.height = height
        self.box_chars = box_chars