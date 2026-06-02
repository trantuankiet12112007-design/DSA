def find_peak(a):
    left = 0
    right = len(a) - 1
    while left < right:
        mid = (left + right) // 2

        if a[mid] < a[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
a = list(map(int, input().split()))
print(find_peak(a))