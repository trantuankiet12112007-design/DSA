def insertion_sort_multi_key(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            if a[j][1] < key[1]:
                a[j + 1] = a[j]
                j -= 1
            elif a[j][1] == key[1] and a[j][0] > key[0]:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    return a

print("Bài 14:", insertion_sort_multi_key([('An', 8), ('Ba', 9), ('Cu', 8)]))