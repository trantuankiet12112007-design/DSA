def insertion_sort_print_steps(a):
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
        print(f"Sau bước {i}: {a}")

print("Bài 4:")
insertion_sort_print_steps([3, 1, 2])