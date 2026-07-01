def count_hash_collisions(keys, m):
    buckets = {}
    collisions = 0
    for key in keys:
        idx = hash(key) % m
        buckets[idx] = buckets.get(idx, 0) + 1

    for count in buckets.values():
        if count > 1:
            collisions += (count - 1)
    return collisions

print("Bài 4 - Số va chạm với m=5:", count_hash_collisions(["apple", "banana", "orange", "grape"], m=5))