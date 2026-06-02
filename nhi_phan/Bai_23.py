def count_less_equal(matrix, value):
    n = len(matrix)
    row = n - 1
    col = 0
    count = 0
    while row >= 0 and col < n:
        if matrix[row][col] <= value:
            count += row + 1
            col += 1
        else:
            row -= 1
    return count


def kth_smallest(matrix, k):
    n = len(matrix)
    left = matrix[0][0]
    right = matrix[n - 1][n - 1]
    result = left
    while left <= right:
        mid = (left + right) // 2
        if count_less_equal(matrix, mid) >= k:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result
n = int(input())
matrix = []
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)
k = int(input())
print(kth_smallest(matrix, k))