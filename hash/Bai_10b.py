import math

def hash_multiplication(key: int, m: int) -> int:
    A = (math.sqrt(5) - 1) / 2
    fractional_part = (key * A) % 1
    return math.floor(m * fractional_part)

print("Bài 10 - Kết quả băm phương pháp nhân cho khoá 500 với m=100:", hash_multiplication(500, m=100))