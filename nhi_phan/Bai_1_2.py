def tuyen_tinh(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1
arr = [15, 25, 80, 30, 60, 50, 110, 100, 130, 180]
x = 110
n = len(arr)
print(tuyen_tinh(arr,n,x))
x = 185
print(tuyen_tinh(arr,n,x))