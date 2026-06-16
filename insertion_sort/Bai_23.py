def analyze_insertion_sort(a):
    n = len(a)
    comparisons = 0
    shifts = 0
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
    return comparisons, shifts

print("Bài 23 (Best):", analyze_insertion_sort([1, 2, 3]))
print("Bài 23 (Worst):", analyze_insertion_sort([3, 2, 1]))