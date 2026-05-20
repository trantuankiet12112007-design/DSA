def ton_tai(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return True
    return False
a = [7, 3, 9, 12, 5, 8, 1]
x = 5
print(ton_tai(a, x))