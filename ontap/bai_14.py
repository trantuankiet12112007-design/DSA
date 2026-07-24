def shell_sort(a, gaps):
    arr = a.copy()
    shifts = 0
    for gap in gaps:
        for i in range(gap, len(arr)):
            key = arr[i]
            j = i
            while j >= gap and arr[j - gap] > key:
                arr[j] = arr[j - gap]
                shifts += 1
                j -= gap
            arr[j] = key
    return arr, shifts


print(shell_sort([9, 8, 3, 7, 5, 6, 4, 1], [4, 2, 1]))
