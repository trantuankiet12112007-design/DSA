def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
arr = [25, 17, 7, 14, 6, 3, 100, -2, -10, -50]
print("Mang chua duoc sap xep la:", arr)
bubbleSort(arr)
print("Mang duoc sap xep la:", arr)