from tuimovedit import *

mov = TUIMov(100,30, "examples/ease_test.tuimov")

for i in range(10):
    box = BoxObject(y=i*3, width=6)
    mov.add_object(box)
    box_tween = box.move_x_tween(90, TUITime(nanoseconds=BILLION//(100+i)*100), sin_ease)
    for _ in range(100+i):
        mov.add_tween(box_tween, move_cursor=True)
        mov.add_action(TUIAction(box.move, (-90,)))
    mov.cursor = ZERO_TIME

mov.render()