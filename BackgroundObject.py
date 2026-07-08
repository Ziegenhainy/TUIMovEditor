from TUIObject import TUIObject

class BackgroundObject(TUIObject):
    def render(self, canvas):
        for i in range(len(canvas)):
            for j in range(len(canvas[0])):
                canvas[i][j] = self.bg_char

    def __init__(self, bg_char=" "):
        self.bg_char = bg_char