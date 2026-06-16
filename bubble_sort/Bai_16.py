def count_inversions_swap(a):
    n = len(a)
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
    return swaps

a = [2, 3, 1]
print(count_inversions_swap(a))