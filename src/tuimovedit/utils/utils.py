from .tuitime import *

BILLION = 1_000_000_000

ZERO_TIME = TUITime()

def time_to_bytes(time: TUITime) -> bytearray:
    return int_to_4_bytes(time.seconds) + int_to_4_bytes(time.nanoseconds)

def int_to_4_bytes(value: int) -> bytearray:
    resultBytes = bytearray()
    for _ in range(4):
        resultBytes.append(value & 0xFF)
        value >>= 8
    return resultBytes