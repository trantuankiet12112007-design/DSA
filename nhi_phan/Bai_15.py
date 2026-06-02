def k_closest_elements(a, k, x):
    left = 0
    right = len(a) - k
    while left < right:
        mid = (left + right) // 2
        if x - a[mid] > a[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return a[left:left + k]
a = list(map(int, input().split()))
k = int(input())
x = int(input())
print(k_closest_elements(a, k, x))