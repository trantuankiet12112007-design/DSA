def tim_kiem_linh_canh(a, x):
    n = len(a)
    a.append(x)
    i = 0
    while a[i] != x:
        i += 1
    a.pop()
    if i < n:
        return i
    return -1
a = [7, 3, 9, 12, 5, 8, 1]
print("Vị trí của 5:", tim_kiem_linh_canh(a, 5))