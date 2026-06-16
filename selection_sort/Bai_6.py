def count_comparisons_selection(a):
    n = len(a)
    comparisons = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return comparisons

print("Bài 6:", count_comparisons_selection([5, 4, 3, 2, 1]))