def count_swaps_fast(a):
    def merge_sort_count(arr):
        if len(arr) <= 1:
            return arr, 0
        mid = len(arr) // 2
        left, inv_left = merge_sort_count(arr[:mid])
        right, inv_right = merge_sort_count(arr[mid:])
        merged, inv_merge = merge_count_split(left, right)
        return merged, inv_left + inv_right + inv_merge

    def merge_count_split(left, right):
        merged = []
        inv_count = 0
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inv_count += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_count

    _, total_swaps = merge_sort_count(a)
    return total_swaps

a = [2, 3, 1]
print(count_swaps_fast(a))