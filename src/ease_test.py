from tuimovedit import *

mov = TUIMov(100,30, "examples/ease_test.tuimov")

for i in range(10):
    box = BoxObject(y=i*3, width=6)
    mov.add_object(box)
    box_tween = box.move_x_tween(90, TUITime(nanoseconds=BILLION//(100+i*2)*100), sin_ease)
    box_tween_2 = box.move_x_tween(-90, TUITime(nanoseconds=BILLION//(100+i*2)*100), sin_ease)
    for j in range(100+i*2):
        mov.add_tween(box_tween if j%2 == 0 else box_tween_2, move_cursor=True)
    mov.cursor = ZERO_TIME

mov.render()