def can_split(a, k, max_sum):
    count = 1
    current_sum = 0
    for num in a:
        if current_sum + num > max_sum:
            count += 1
            current_sum = num
        else:
            current_sum += num
    return count <= k


def split_array(a, k):
    left = max(a)
    right = sum(a)
    result = right
    while left <= right:
        mid = (left + right) // 2
        if can_split(a, k, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result
a = list(map(int, input().split()))
k = int(input())
print(split_array(a, k))