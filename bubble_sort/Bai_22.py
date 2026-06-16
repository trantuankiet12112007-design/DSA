def count_passes_k_deviation(a):
    n = len(a)
    passes = 0
    for i in range(n):
        swapped = False
        passes += 1
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return passes

a = [1, 3, 2, 5, 4, 7, 6] 
print(count_passes_k_deviation(a))