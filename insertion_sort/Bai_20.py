def shell_sort(a):
    n = len(a)
    gap = n // 2
    shifts = 0
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]
            j = i
            while j >= gap and a[j - gap] > temp:
                a[j] = a[j - gap]
                shifts += 1
                j -= gap
            a[j] = temp
        gap //= 2
    return a, shifts

print("Bài 20 (Mảng, Số shift):", shell_sort([8, 7, 6, 5, 4, 3, 2, 1]))