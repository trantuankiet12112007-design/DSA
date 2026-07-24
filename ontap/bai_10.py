import bisect

def binary_insertion_sort(a):
    arr = a.copy()
    shifts = 0
    for i in range(1, len(arr)):
        key = arr[i]

        pos = bisect.bisect_right(arr[:i], key)

        shifts += (i - pos)
        arr[pos+1:i+1] = arr[pos:i]
        arr[pos] = key
    return arr, shifts

print(binary_insertion_sort([3, 2, 1]))
