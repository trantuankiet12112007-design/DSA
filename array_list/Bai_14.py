class Dynamic2DArray:
    def __init__(self):
        self.matrix = []

    def add_row(self, row_data):
        self.matrix.append(row_data)

    def get(self, i, j):
        return self.matrix[i][j]

    def set(self, i, j, val):
        self.matrix[i][j] = val

matrix_2d = Dynamic2DArray()
matrix_2d.add_row([1, 2, 3])
matrix_2d.add_row([4, 5, 6])
matrix_2d.set(1, 1, 99)
print("Bài 14 - Tra cứu ô (1,1):", matrix_2d.get(1, 1))