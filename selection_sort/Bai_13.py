def selection_sort_students(a):
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j][1] < a[min_idx][1]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

print("Bài 13:", selection_sort_students([('An', 8), ('Ba', 5)]))