import random

class UniversalHashFamily:
    def __init__(self, m=10, p=1000003):
        self.m = m
        self.p = p
        self.a = random.randint(1, p - 1)
        self.b = random.randint(0, p - 1)

    def hash(self, key: int) -> int:
        return ((self.a * key + self.b) % self.p) % self.m

uhf = UniversalHashFamily()
print("Bài 9 - Giá trị băm phổ quát cho khoá 12345:", uhf.hash(12345))