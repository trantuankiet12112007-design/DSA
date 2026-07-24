def selection_sort(a):
    arr = a.copy()
    n = len(arr)
    comparisons = 0
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr, comparisons

print(selection_sort([5, 4, 3, 2, 1]))
