def rotate_array(arr, k):
    n = len(arr)
    k = k % n

    def reverse_sub(left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    reverse_sub(0, n - 1)
    reverse_sub(0, k - 1)
    reverse_sub(k, n - 1)
    return arr

print("Bài 11:", rotate_array([1, 2, 3, 4, 5], k=2))