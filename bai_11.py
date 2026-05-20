def tim_lon_nhat(a):
    max_value = a[0]
    vi_tri = 0
    for i in range(1, len(a)):
        if a[i] > max_value:
            max_value = a[i]
            vi_tri = i
    return max_value, vi_tri
a = [7, 3, 15, 9, 2]
print(tim_lon_nhat(a))