def two_sum_hash(arr, target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return None

print("Bài 9:", two_sum_hash([2, 7, 11], 9))