def lower_bound(a, x):
    left = 0
    right = len(a)
    while left < right:
        mid = (left + right) // 2

        if a[mid] >= x:
            right = mid
        else:
            left = mid + 1
    return left
a = list(map(int, input().split()))
x = int(input())
print(lower_bound(a, x))