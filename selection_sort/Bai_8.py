def find_min_index(a, i):
    min_idx = i
    for j in range(i + 1, len(a)):
        if a[j] < a[min_idx]:
            min_idx = j
    return min_idx

print("Bài 8:", find_min_index([9, 3, 7, 1, 5], 1))