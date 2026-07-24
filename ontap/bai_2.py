def find_first_last_count(a, x):
    def find_first():
        l, r, res = 0, len(a) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if a[mid] == x:
                res = mid
                r = mid - 1
            elif a[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return res

    def find_last():
        l, r, res = 0, len(a) - 1, -1
        while l <= r:
            mid = (l + r) // 2
            if a[mid] == x:
                res = mid
                l = mid + 1
            elif a[mid] < x:
                l = mid + 1
            else:
                r = mid - 1
        return res

    first = find_first()
    if first == -1:
        return -1, -1, 0
    last = find_last()
    return first, last, last - first + 1

first, last, count = find_first_last_count([1, 2, 2, 2, 3], 2)
print(f"dau={first}, cuoi={last}, dem={count}")
