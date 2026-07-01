def remove_if_even(arr):
    write_idx = 0
    for read_idx in range(len(arr)):
        if arr[read_idx] % 2 != 0:
            arr[write_idx] = arr[read_idx]
            write_idx += 1
    del arr[write_idx:]
    return arr


print("Bài 8:", remove_if_even([1, 2, 3, 4]))