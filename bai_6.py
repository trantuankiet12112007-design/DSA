def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1
a = [7, 3, 9, 12, 5, 8, 1]
x = 5
print(linear_search(a, x))