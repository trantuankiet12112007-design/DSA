def hash_string_sum(s: str, m: int) -> int:
    total_ascii = sum(ord(char) for char in s)
    return total_ascii % m

print("Bài 2 (Chuỗi 'abc'):", hash_string_sum("abc", 100))
print("Bài 2 (Chuỗi đảo 'cba'):", hash_string_sum("cba", 100))