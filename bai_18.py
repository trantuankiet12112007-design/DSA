def tim_kiem_ma_tran(M, x):
    so_dong = len(M)
    so_cot = len(M[0]) if so_dong > 0 else 0
    for i in range(so_dong):
        for j in range(so_cot):
            if M[i][j] == x:
                return (i, j)
    return (-1, -1)
M = [[5, 8, 1], [3, 9, 7], [2, 6, 4]]
print("Vị trí của 9:", tim_kiem_ma_tran(M, 9))