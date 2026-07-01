def hash_combine_tuple(a, b) -> int:
    h_a = hash(a)
    h_b = hash(b)
    return h_a ^ (h_b + 0x9e3779b9 + (h_a << 6) + (h_a >> 2))

print("Bài 7 - Hash cặp (1, 2):", hash_combine_tuple(1, 2))
print("Bài 7 - Hash cặp đối xứng (2, 1):", hash_combine_tuple(2, 1))