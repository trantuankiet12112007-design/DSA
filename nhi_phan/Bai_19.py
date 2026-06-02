def can_place(stalls, cows, distance):
    count = 1
    last_position = stalls[0]
    for i in range(1, len(stalls)):
        if stalls[i] - last_position >= distance:
            count += 1
            last_position = stalls[i]

            if count >= cows:
                return True
    return False
def aggressive_cows(stalls, cows):
    stalls.sort()

    left = 1
    right = stalls[-1] - stalls[0]
    result = 0
    while left <= right:
        mid = (left + right) // 2

        if can_place(stalls, cows, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result
stalls = list(map(int, input().split()))
cows = int(input())
print(aggressive_cows(stalls, cows))