def bubble_sort_stable(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j][0] > arr[j + 1][0]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [(2, 'a'), (1, 'b'), (2, 'c')]
print("Bài 13 - Trước khi sắp xếp:", arr)
print("Bài 13 - Sau khi sắp xếp:  ", bubble_sort_stable(arr))