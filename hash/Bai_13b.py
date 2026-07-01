def hash_2d_matrix(matrix, p=31, q=37, mod=10 ** 9 + 7):
    row_hashes = []
    for row in matrix:
        h_row = 0
        for val in row:
            h_row = (h_row * p + val) % mod
        row_hashes.append(h_row)

    final_hash = 0
    for rh in row_hashes:
        final_hash = (final_hash * q + rh) % mod
    return final_hash

sample_matrix = [
    [1, 2],
    [3, 4]
]
print("Bài 13 - Mã băm ma trận hai chiều:", hash_2d_matrix(sample_matrix))