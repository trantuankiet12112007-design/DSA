def intersection_of_arrays(arr1, arr2):
    set1 = set(arr1)
    result = [item for item in arr2 if item in set1]
    return list(set(result))

print("Bài 4:", intersection_of_arrays([1, 2, 3], [2, 3, 4]))