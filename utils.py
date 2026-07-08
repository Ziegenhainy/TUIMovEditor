BILLION = 1_000_000_000

def time_to_bytes(seconds: int = 0, nanoseconds: int = 0) -> bytearray:
    return int_to_4_bytes(seconds) + int_to_4_bytes(nanoseconds)

def int_to_4_bytes(value: int) -> bytearray:
    resultBytes = bytearray()
    for _ in range(4):
        resultBytes.append(value & 0xFF)
        value >>= 8
    return resultBytes