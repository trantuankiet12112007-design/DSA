def can_place_magnets(positions, m, distance):
    count = 1
    last_position = positions[0]
    for i in range(1, len(positions)):
        if positions[i] - last_position >= distance:
            count += 1
            last_position = positions[i]
            if count >= m:
                return True
    return False


def max_magnetic_force(positions, m):
    positions.sort()
    left = 1
    right = positions[-1] - positions[0]
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if can_place_magnets(positions, m, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

positions = list(map(int, input().split()))
m = int(input())
print(max_magnetic_force(positions, m))