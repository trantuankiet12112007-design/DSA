def optimized_bubble_sort(a):
    n = len(a)
    arr = a.copy()
    passes = 0
    for i in range(n):
        swapped = False
        passes += 1
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr, passes


print(optimized_bubble_sort([1, 2, 3, 4]))
