def hash_polynomial(s: str, p=31, m=10**9 + 7) -> int:
    hash_val = 0
    for char in s:
        hash_val = (hash_val * p + ord(char)) % m
    return hash_val

print("Bài 3 (Chuỗi 'abc'):", hash_polynomial("abc"))
print("Bài 3 (Chuỗi 'cba'):", hash_polynomial("cba"))