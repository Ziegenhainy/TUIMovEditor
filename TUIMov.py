from utils import *
from TUIObject import *
from TextObject import *
from TUIAction import *
from BackgroundObject import *
from TUITween import *
from tuitime import *

class TUIMov:
    def render(self):
        self.actions.sort(key=lambda a: a.time)
        # TODO: sort the shit

        cur_time = TUITime()
        frame_time = TUITime()
        for action in self.actions:
            for obj in self.objects:
                obj.render(self.canvas)

            next_frame = "\033[H"
            for line in self.canvas:
                for c in line:
                    next_frame += c
                next_frame += "\n"
            
            action.action_func(*action.action_args)
            
            frame_time = action.time-cur_time
            cur_time = action.time
            if frame_time:
                self.add_string(next_frame)
                self.add_pause(frame_time)



    def add_string(self, new_str: str):
        self.file.write(bytes(new_str, encoding="UTF-8"))

    def add_pause(self, time: TUITime = TUITime()):
        self.file.write(bytes([0]))
        self.file.write(time_to_bytes(time))

    def add_object(self, new_obj: TUIObject):
        self.objects.append(new_obj)

    def add_action(self, new_act: TUIAction):
        self.actions.append(new_act)


    def add_tween(self, tween: TUITween, start_time: TUITime):
        for step in range(tween.end_val):
            next_action = TUIAction(tween.frame_handler, (step,), start_time+(tween.time*tween.ease_func(step/tween.end_val)))
            self.add_action(next_action)

    def add_tweens(self, tweens: tuple[TUITween], start_time: TUITime):
        for tween in tweens:
            self.add_tween(tween, start_time)

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