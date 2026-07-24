def split_array(a, k):
    def can_split(max_sum):
        count = 1
        current_sum = 0
        for x in a:
            if current_sum + x > max_sum:
                count += 1
                current_sum = x
            else:
                current_sum += x
        return count <= k

    l, r = max(a), sum(a)
    res = r
    while l <= r:
        mid = (l + r) // 2
        if can_split(mid):
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

print(split_array([7, 2, 5, 10, 8], 2)) 
