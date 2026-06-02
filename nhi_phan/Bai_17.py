def can_ship(weights, D, capacity):
    days = 1
    current_weight = 0
    for w in weights:
        if current_weight + w > capacity:
            days += 1
            current_weight = w
        else:
            current_weight += w
    return days <= D
def ship_capacity(weights, D):
    left = max(weights)
    right = sum(weights)
    result = right
    while left <= right:
        mid = (left + right) // 2

        if can_ship(weights, D, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result
weights = list(map(int, input().split()))
D = int(input())
print(ship_capacity(weights, D))