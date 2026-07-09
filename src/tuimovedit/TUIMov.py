from .objects import *
from .TUIAction import *
from .TUITween import *
from .utils import *

class TUIMov:
    def render_frame(self):
        self.frames_rendered += 1
        if self.frames_rendered % 10 == 0 or self.num_actions_done == self.num_actions:
            print(f"\rFrame: {self.frames_rendered:5d}, Action: {self.num_actions_done:5d}/{self.num_actions}, Pass: {self.render_pass}", end="")
        for obj in self.objects:
            obj.render(self.canvas)


        next_frame = "\033[H"
        for line in self.canvas:
            for c in line:
                next_frame += c
            next_frame += "\n"
        self.add_string(next_frame)
        

    def render(self):
        self.render_pass += 1
        self.actions.sort(key=lambda a: a.time)
        # TODO: sort the shit

        cur_time = TUITime()
        frame_time = TUITime()
        self.num_actions = len(self.actions)
        self.num_actions_done = 0
        for action in self.actions:
            self.num_actions_done += 1
            action.action_func(*action.action_args)
            
            frame_time = action.time-cur_time
            cur_time = action.time
            if frame_time:
                self.render_frame()
                self.add_pause(frame_time)
        if not frame_time:
            self.render_frame()
        print(" Done! :3")



    def add_string(self, new_str: str):
        self.file.write(bytes(new_str, encoding="UTF-8"))

    def add_pause(self, time: TUITime = TUITime()):
        self.file.write(bytes([0]))
        self.file.write(time_to_bytes(time))

    def add_object(self, new_obj: TUIObject):
        self.objects.append(new_obj)

    def add_action(self, new_act: TUIAction, move_cursor=False):
        new_act.time += self.cursor
        self.actions.append(new_act)
        if move_cursor:
            self.cursor = new_act.time


    def add_tween(self, tween: TUITween, move_cursor = False):
        for step in range(tween.end_val):
            next_time = tween.time*tween.ease_func(step/tween.end_val)
            next_action = TUIAction(tween.frame_handler, (step,), next_time)
            self.add_action(next_action)
        if move_cursor:
            self.cursor += tween.time

    def add_tweens(self, tweens: tuple[TUITween], move_cursor = False):
        for tween in tweens:
            self.add_tween(tween)
        if move_cursor:
            self.cursor += tweens[0].time

    def __init__(self, width, height, filepath, add_background=True):
        self.filepath = filepath
        self.file = open(filepath, "wb")
        self.width = width
        self.height = height
        self.canvas: list[list[str]] = [[" " for _ in range(width)] for _ in range(height)]
        self.objects: list[TUIObject] = []
        self.actions: list[TUIAction] = []
        self.background = None 
        self.cursor = TUITime()

        self.render_pass = 0
        self.frames_rendered = 0
        self.num_actions = 0
        self.num_actions_done = 0

        if add_background:
            self.background = BackgroundObject()
            self.objects.append(self.background)