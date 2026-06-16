def bubble_sort_optimized(a):
    n = len(a)
    passes = 0
    
    for i in range(n):
        swapped = False
        passes += 1 
        
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
                
        if not swapped:
            break
            
    return passes

a_sorted = [1, 2, 3, 4]
so_luot = bubble_sort_optimized(a_sorted)
print(f"Bài 9 - Số lượt chạy với mảng đã sắp xếp: {so_luot}") 