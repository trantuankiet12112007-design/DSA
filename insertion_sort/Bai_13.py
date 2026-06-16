def insertion_sort_stable(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j][0] > key[0]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

print("Bài 13:", insertion_sort_stable([(2, 'a'), (1, 'b'), (2, 'c')]))