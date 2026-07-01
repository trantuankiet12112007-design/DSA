def remove_duplicates_preserve_order(arr):
    seen = set()
    result = []
    for x in arr:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

print("Bài 12:", remove_duplicates_preserve_order([3, 1, 3, 2, 1]))