def kth_missing_positive(a, k):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        missing = a[mid] - (mid + 1)
        if missing < k:
            left = mid + 1
        else:
            right = mid - 1
    return left + k
a = list(map(int, input().split()))
k = int(input())
print(kth_missing_positive(a, k))