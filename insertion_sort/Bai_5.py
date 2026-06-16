def count_shifts(a):
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

print("Bài 5:", count_shifts([3, 2, 1]))