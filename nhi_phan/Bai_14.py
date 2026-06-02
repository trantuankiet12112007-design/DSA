def search_matrix(matrix, x):
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n - 1
    while left <= right:
        mid = (left + right) // 2
        row = mid // n
        col = mid % n
        if matrix[row][col] == x:
            return True
        elif matrix[row][col] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False
m, n = map(int, input().split())
matrix = []
for i in range(m):
    row = list(map(int, input().split()))
    matrix.append(row)
x = int(input())
print(search_matrix(matrix, x))