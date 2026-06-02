def first_position(a, x):
    left = 0
    right = len(a) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            result = mid
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return result
a = list(map(int, input().split()))
x = int(input())
print(first_position(a, x))