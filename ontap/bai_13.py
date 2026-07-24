def count_inversions(a):
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_l = merge_sort(arr[:mid])
        right, inv_r = merge_sort(arr[mid:])
        
        merged = []
        i = j = 0
        inv_split = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_split += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        
        return merged, inv_l + inv_r + inv_split

    _, total_inversions = merge_sort(a)
    return total_inversions

print(count_inversions([2, 3, 1, 5, 4]))
