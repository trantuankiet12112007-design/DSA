def double_selection_sort(a):
    n = len(a)
    left, right = 0, n - 1
    while left < right:
        min_idx = left
        max_idx = left
        for i in range(left, right + 1):
            if a[i] < a[min_idx]:
                min_idx = i
            elif a[i] > a[max_idx]:
                max_idx = i
                
        a[left], a[min_idx] = a[min_idx], a[left]
        if max_idx == left:
            max_idx = min_idx
        a[right], a[max_idx] = a[max_idx], a[right]
        
        left += 1
        right -= 1
    return a

print("Bài 9:", double_selection_sort([5, 1, 4, 2, 8]))