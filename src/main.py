from tuimovedit import *


def main():
    mov = TUIMov(80, 30, "test.tuimov")

    text1 = TextObject(0, 0, "Hiii")
    text2 = TextObject(60,10, "Hello, Text!")
    text3 = TextObject(-5, 20, "im Stupid lol")
    
    box1 = BoxObject(x=3, y=3, width=10, height=1)
    mov.add_object(box1)

    text4 = TextObject(10, -20, "UwU")
    
    mov.add_object(text1)
    mov.add_object(text2)
    mov.add_object(text3)
    mov.add_object(text4)
    for i in range(1,100):
        mov.add_action(TUIAction(text1.move, (0,1), TUITime(nanoseconds=BILLION//30)), True)
        mov.add_action(TUIAction(text2.move, (-1,0)))
        mov.add_action(TUIAction(text3.move, (1,0)))
    
    mov.cursor = TUITime()
    mov.add_action(TUIAction(text4.move, (0, 30),TUITime(1,0)))

    uwu_tweens = text4.move_tween(10,20, TUITime(3))
    mov.cursor = TUITime(1,BILLION//2)
    mov.add_tweens(uwu_tweens)

    mov.cursor = TUITime()
    box_tween = box1.move_x_tween(40, TUITime(1))
    mov.add_tween(box_tween, move_cursor=True)
    box_tween = box1.move_y_tween(10, TUITime(1))
    mov.add_tween(box_tween, move_cursor=True)
    box_tween = box1.move_x_tween(-40, TUITime(1))
    mov.add_tween(box_tween, move_cursor=True)
    box_tween = box1.move_y_tween(-10, TUITime(1))
    mov.add_tween(box_tween, move_cursor=True)
    
    mov.cursor = TUITime()
    mov.add_action(TUIAction(box1.size, (4,2), TUITime(1)))

    mov.render()

if __name__ == "__main__":
    main()