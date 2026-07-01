def evaluate_hash_distribution(keys, m, hash_func_wrapper):
    buckets = [0] * m
    for key in keys:
        idx = hash_func_wrapper(key) % m
        buckets[idx] += 1
    mean_val = len(keys) / m
    variance_score = sum((count - mean_val) ** 2 for count in buckets)
    return variance_score

sample_keys = [f"user_{i}" for i in range(100)]
score = evaluate_hash_distribution(sample_keys, m=10, hash_func_wrapper=hash)
print("Bài 8 - Điểm độ lệch phân bố của hàm tích hợp (Càng nhỏ càng đều):", score)