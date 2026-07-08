from TUIMov import *


def main():
    mov = TUIMov(80, 30, "test.tuimov")
    
    text1 = TextObject(0, 0, "Hiii")
    text2 = TextObject(60,10, "Hello, Text!")
    text3 = TextObject(-5, 20, "im Stupid lol")

    mov.add_object(text1)
    mov.add_object(text2)
    mov.add_object(text3)
    for _ in range(100):
        mov.add_action(TUIAction(text1.move, (0,1), nanoseconds=BILLION//30))
        mov.add_action(TUIAction(text2.move, (-1,0), seconds=0))
        mov.add_action(TUIAction(text3.move, (1,0), seconds=0))
    mov.render()

if __name__ == "__main__":
    main()