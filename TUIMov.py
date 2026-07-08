from utils import *
from TUIObject import *
from TextObject import *
from TUIAction import *
from BackgroundObject import *

class TUIMov:
    def render(self):
        for action in self.actions:
            for obj in self.objects:
                obj.render(self.canvas)

            next_frame = "\033[H"
            for line in self.canvas:
                for c in line:
                    next_frame += c
                next_frame += "\n"
            
            action.action_func(*action.action_args)
            
            if action.seconds or action.nanoseconds:
                self.add_string(next_frame)
                self.add_pause(action.seconds, action.nanoseconds)



    def add_string(self, new_str: str):
        self.file.write(bytes(new_str, encoding="UTF-8"))

    def add_pause(self, seconds=0, nanoseconds=0):
        self.file.write(bytes([0]))
        self.file.write(time_to_bytes(seconds, nanoseconds))

    def add_object(self, new_obj: TUIObject):
        self.objects.append(new_obj)

    def add_action(self, new_act: TUIAction):
        self.actions.append(new_act)

    def __init__(self, width, height, filepath, add_background=True):
        self.filepath = filepath
        self.file = open(filepath, "wb")
        self.width = width
        self.height = height
        self.canvas: list[list[str]] = [[" " for _ in range(width)] for _ in range(height)]
        self.objects: list[TUIObject] = []
        self.actions: list[TUIAction] = []
        self.background = None 

        if add_background:
            self.background = BackgroundObject()
            self.objects.append(self.background)