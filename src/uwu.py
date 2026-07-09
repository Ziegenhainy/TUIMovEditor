from tuimovedit import *

mov = TUIMov(60,30, "uwu.tuimov")

box1 = BoxObject(width=10,height=5)
mov.add_object(box1)

box_tween = box1.move_tween(40, 20, TUITime(1))
mov.add_tweens(box_tween)

mov.render()