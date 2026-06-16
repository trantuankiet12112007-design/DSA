def count_comparisons(a):
    n = len(a)
    comparisons = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = key
    return comparisons

print("Bài 6:", count_comparisons([1, 2, 3]))