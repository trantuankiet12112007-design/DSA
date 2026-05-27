def tim_min_max(a):
    min_value = a[0]
    max_value = a[0]
    for value in a:
        if value < min_value:
            min_value = value
        if value > max_value:
            max_value = value
    return min_value, max_value
a = [7, 3, 15, 9, 2]
print(tim_min_max(a))