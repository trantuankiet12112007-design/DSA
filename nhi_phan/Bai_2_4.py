def binary_search(arr, key):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1
arr = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
key = 16
result = binary_search(arr, key)
print("Vi tri tim kiem la:", result)
key = 16
result = binary_search(arr, key)
print("Vi tri tim kiem la:", result)