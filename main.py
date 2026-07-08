from TUIMov import *


def main():
    mov = TUIMov(80, 30, "test.tuimov")
    
    text1 = TextObject(0, 0, "Hiii")
    text2 = TextObject(60,10, "Hello, Text!")
    text3 = TextObject(-5, 20, "im Stupid lol")

    text4 = TextObject(10, -20, "UwU")

    mov.add_object(text1)
    mov.add_object(text2)
    mov.add_object(text3)
    mov.add_object(text4)
    for i in range(1,100):
        next_frame_time = TUITime(nanoseconds=BILLION//30)*i
        mov.add_action(TUIAction(text1.move, (0,1), next_frame_time))
        mov.add_action(TUIAction(text2.move, (-1,0), next_frame_time))
        mov.add_action(TUIAction(text3.move, (1,0), next_frame_time))
    
    mov.add_action(TUIAction(text4.move, (0, 30),TUITime(1,0)))

    uwu_tweens = text4.move_tween(10,20, TUITime(3))
    mov.add_tweens(uwu_tweens, TUITime(1,BILLION//2))

    mov.render()

if __name__ == "__main__":
    main()