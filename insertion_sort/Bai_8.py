def insertion_sort_k_steps(a, k):
    n = len(a)
    for i in range(1, min(k + 1, n)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

print("Bài 8:", insertion_sort_k_steps([4, 3, 2, 1], 1))