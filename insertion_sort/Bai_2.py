def insertion_sort_basic(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

print("Bài 2:", insertion_sort_basic([5, 2, 4, 6, 1, 3])) 