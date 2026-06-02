def ton_tai(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            return True
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False
a = list(map(int, input().split()))
x = int(input())
print(ton_tai(a, x))