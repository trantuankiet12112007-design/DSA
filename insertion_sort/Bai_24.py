def compare_three_sorts(a):
    def count_insertion(arr):
        comp = shifts = 0
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0:
                comp += 1
                if arr[j] > key:
                    arr[j + 1] = arr[j]
                    shifts += 1
                    j -= 1
                else:
                    break
            arr[j + 1] = key
        return comp, shifts
        
    def count_bubble(arr):
        comp = swaps = 0
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                comp += 1
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swaps += 1
                    swapped = True
            if not swapped: break
        return comp, swaps
        
    def count_selection(arr):
        comp = swaps = 0
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                comp += 1
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                arr[i], arr[min_idx] = arr[min_idx], arr[i]
                swaps += 1
        return comp, swaps

    return {
        "Insertion": count_insertion(list(a)),
        "Bubble": count_bubble(list(a)),
        "Selection": count_selection(list(a))
    }

print("Bài 24:", compare_three_sorts([3, 2, 1, 4, 5]))