from tuimovedit import *
import random as rd

WIDTH = 232
HEIGHT = 63

mov = TUIMov(WIDTH,HEIGHT, "examples/uwu.tuimov")

transparent_box=(
    "╔═╗",
    "║\0║",
    "╚═╝")
for j in range(20):
    for i in range(60):
        box = BoxObject(
            0,
            0,
            rd.randint(3,30),
            rd.randint(2,15),
            transparent_box)
        box.move(rd.randint(-box.width, WIDTH),rd.randint(-box.height, HEIGHT))
        mov.add_object(box)
        mov.add_tweens(box.move_tween(rd.randint(-box.x-box.width,WIDTH-box.x),rd.randint(-box.y-box.height,HEIGHT-box.y), TUITime(3), sin_ease if rd.randint(0,1) else linear_ease))
        

    mov.render()