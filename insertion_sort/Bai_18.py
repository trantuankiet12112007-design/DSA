def compare_search_directions(a):
    n = len(a)
    comp_right_to_left = 0
    comp_left_to_right = 0
    
    a1 = list(a)
    for i in range(1, n):
        key = a1[i]
        j = i - 1
        while j >= 0:
            comp_right_to_left += 1
            if a1[j] > key:
                a1[j + 1] = a1[j]
                j -= 1
            else:
                break
        a1[j + 1] = key
        
    a2 = list(a)
    for i in range(1, n):
        key = a2[i]
        pos = 0
        while pos < i:
            comp_left_to_right += 1
            if a2[pos] > key:
                break
            pos += 1
        for j in range(i - 1, pos - 1, -1):
            a2[j + 1] = a2[j]
        a2[pos] = key
        
    return comp_right_to_left, comp_left_to_right

print("Bài 18 (Số so sánh R->L, L->R):", compare_search_directions([1, 2, 4, 3, 5]))