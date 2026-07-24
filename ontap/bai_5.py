import math

def min_eating_speed(piles, h):
    def can_eat(speed):
        return sum(math.ceil(p / speed) for p in piles) <= h

    l, r = 1, max(piles)
    res = r
    while l <= r:
        mid = (l + r) // 2
        if can_eat(mid):
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    return res

print(min_eating_speed([3, 6, 7, 11], 8))