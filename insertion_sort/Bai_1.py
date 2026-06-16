def insert_element(a, x):
    a.append(x)
    i = len(a) - 1
    while i > 0 and a[i - 1] > x:
        a[i] = a[i - 1]
        i -= 1
    a[i] = x
    return a

print("Bài 1:", insert_element([1, 3, 5, 7], 4))