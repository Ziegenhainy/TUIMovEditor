BILLION = 1_000_000_000

class TUITime:
    def __add__(a: TUITime, b: TUITime):
        return TUITime(
            a.seconds + b.seconds + (a.nanoseconds+b.nanoseconds)//BILLION,
            (a.nanoseconds + b.nanoseconds) % BILLION
        )
    
    def __lt__(self: TUITime, other: TUITime):
        return (self.seconds < other.seconds) or (
                self.seconds == other.seconds and 
                self.nanoseconds < other.nanoseconds)

    def __sub__(a: TUITime, b: TUITime):
        a = a.seconds*BILLION+a.nanoseconds
        b = b.seconds*BILLION+b.nanoseconds
        result = max(a-b,0)
        return TUITime(
            result // BILLION,
            result %  BILLION
        )

    def __mul__(a, b):
        a = a.seconds*BILLION+a.nanoseconds if isinstance(a, TUITime) else a
        b = b.seconds*BILLION+b.nanoseconds if isinstance(b, TUITime) else b
        result = a*b
        return TUITime(
            result // BILLION,
            result %  BILLION
        )

    def __bool__(self):
        return bool(self.seconds or self.nanoseconds)

    def __init__(self, seconds=0, nanoseconds=0):
        self.seconds = int(seconds)
        self.nanoseconds = int(nanoseconds)