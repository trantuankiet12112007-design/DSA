def hash_order_independent(elements_set) -> int:
    return sum(hash(item) for item in elements_set)

set_a = [1, 2, 3]
set_b = [3, 1, 2]
print("Bài 11 - Trùng mã băm không?:", hash_order_independent(set_a) == hash_order_independent(set_b))