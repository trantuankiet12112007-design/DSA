def lower_bound(a, x):
    l, r, res = 0, len(a) - 1, len(a)
    while l <= r:
        mid = (l + r) // 2
        if a[mid] >= x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

def upper_bound(a, x):
    l, r, res = 0, len(a) - 1, len(a)
    while l <= r:
        mid = (l + r) // 2
        if a[mid] > x:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

a = [1, 3, 5, 7]
print("lower_bound idx:", lower_bound(a, 4))
