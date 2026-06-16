def analyze_performance(a):
    n = len(a)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break
    return comparisons, swaps

a_best = [1, 2, 3, 4, 5]
a_worst = [5, 4, 3, 2, 1]

print(analyze_performance(a_best))
print(analyze_performance(a_worst))