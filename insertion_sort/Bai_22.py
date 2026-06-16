def insertion_sort_k_deviation(a):
    n = len(a)
    shifts = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            shifts += 1
            j -= 1
        a[j + 1] = key
    return shifts

print("Bài 22:", insertion_sort_k_deviation([1, 3, 2, 5, 4, 7, 6]))