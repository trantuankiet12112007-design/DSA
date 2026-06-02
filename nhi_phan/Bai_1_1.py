def tuyen_tinh(arr, n, x):
    for i in range(0, n):
        if arr[i] == x:
            return i
    return -1
arr = [20, 30, 15, 5, 10, 40]
x = 40
n = len(arr)
print(tuyen_tinh(arr,n,x))