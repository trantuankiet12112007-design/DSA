def can_eat(piles, h, speed):
    total_hours = 0
    for pile in piles:
        total_hours += (pile + speed - 1) // speed
    return total_hours <= h
def min_eating_speed(piles, h):
    left = 1
    right = max(piles)
    result = right
    while left <= right:
        mid = (left + right) // 2
        if can_eat(piles, h, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result
piles = list(map(int, input().split()))
h = int(input())
print(min_eating_speed(piles, h))