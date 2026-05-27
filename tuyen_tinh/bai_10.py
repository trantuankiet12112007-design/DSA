def vi_tri_cuoi(a, x):
    for i in range(len(a) - 1, -1, -1):
        if a[i] == x:
            return i
    return -1
a = [2, 5, 7, 5, 9]
x = 5
print(vi_tri_cuoi(a, x))