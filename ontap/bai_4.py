def search_rotated(a, x):
    l, r = 0, len(a) - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == x:
            return mid

        if a[l] <= a[mid]:
            if a[l] <= x < a[mid]:
                r = mid - 1
            else:
                l = mid + 1

        else:
            if a[mid] < x <= a[r]:
                l = mid + 1
            else:
                r = mid - 1
    return -1


print(search_rotated([4, 5, 6, 7, 0, 1, 2], 0))
