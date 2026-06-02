import math
def can_place_gas_stations(stations, k, max_distance):
    needed = 0

    for i in range(1, len(stations)):
        distance = stations[i] - stations[i - 1]
        needed += math.ceil(distance / max_distance) - 1

    return needed <= k

def minimize_max_distance(stations, k):
    left = 0
    right = stations[-1] - stations[0]
    for _ in range(100):
        mid = (left + right) / 2

        if can_place_gas_stations(stations, k, mid):
            right = mid
        else:
            left = mid
    return right

stations = list(map(float, input().split()))
k = int(input())
print(f"{minimize_max_distance(stations, k):.6f}")