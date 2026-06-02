def single_non_duplicate(a):
    left = 0
    right = len(a) - 1
    while left < right:
        mid = (left + right) // 2
        if mid % 2 == 1:
            mid -= 1

        if a[mid] == a[mid + 1]:
            left = mid + 2
        else:
            right = mid
    return a[left]
a = list(map(int, input().split()))
print(single_non_duplicate(a))