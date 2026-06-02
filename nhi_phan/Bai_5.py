def first_position(a, x):
    left = 0
    right = len(a) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if a[mid] == x:
            result = mid
            right = mid - 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return result


def last_position(a, x):
    left = 0
    right = len(a) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            result = mid
            left = mid + 1
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return result
def count_x(a, x):
    first = first_position(a, x)
    if first == -1:
        return 0
    last = last_position(a, x)
    return last - first + 1
a = list(map(int, input().split()))
x = int(input())
print(count_x(a, x))