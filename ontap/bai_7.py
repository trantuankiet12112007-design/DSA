def bubble_sort(a):
    n = len(a)
    swaps = 0
    arr = a.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return arr, swaps


print(bubble_sort([2, 3, 1]))
