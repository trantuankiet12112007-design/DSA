def binary_insertion_sort(a):
    n = len(a)
    comparisons = 0
    for i in range(1, n):
        key = a[i]
        left, right = 0, i - 1
        while left <= right:
            comparisons += 1
            mid = (left + right) // 2
            if a[mid] > key:
                right = mid - 1
            else:
                left = mid + 1
        for j in range(i - 1, left - 1, -1):
            a[j + 1] = a[j]
        a[left] = key
    return a, comparisons

print("Bài 9:", binary_insertion_sort([5, 2, 4, 6, 1, 3]))