from tuimovedit import *
import random as rd

mov = TUIMov(200,100, "uwu.tuimov")

transparent_box=(
    "╔═╗",
    "║\0║",
    "╚═╝")
for j in range(20):
    for i in range(40):
        box = BoxObject(
            rd.randint(0,200),
            rd.randint(0,100),
            rd.randint(3,30),
            rd.randint(2,15),
            transparent_box)
        mov.add_object(box)
        mov.add_tweens(box.move_tween(rd.randint(-100,100),rd.randint(-50,50), TUITime(3)))
        

    mov.render()
    mov.objects = [BackgroundObject()]
    mov.actions = []