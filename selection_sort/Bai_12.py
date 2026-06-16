def stable_selection_sort(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][0] < a[min_idx][0]:
                min_idx = j
                
        min_val = a[min_idx]
        while min_idx > i:
            a[min_idx] = a[min_idx - 1]
            min_idx -= 1
        a[i] = min_val
        
    return a

print("Bài 12:", stable_selection_sort([(2, 'a'), (2, 'b'), (1, 'c')]))