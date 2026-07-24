def binary_search(a, x):
    l, r = 0, len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9], 7))
