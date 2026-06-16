def count_swaps_selection(a):
    n = len(a)
    swaps = 0
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
    return swaps

print("Bài 5:", count_swaps_selection([3, 2, 1]))