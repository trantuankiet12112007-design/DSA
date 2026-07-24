import random

class UniversalHash:
    def __init__(self, m, p=10000019):
        self.m = m
        self.p = p
        self.a = random.randint(1, p - 1)
        self.b = random.randint(0, p - 1)

    def hash(self, k):
        return ((self.a * k + self.b) % self.p) % self.m

uh = UniversalHash(10)
print("Câu 49 (Hash xain 12345):", uh.hash(12345))
