def count_even_elements(arr):
    count = 0
    for x in arr:
        if x % 2 == 0:
            count += 1
    return count


print("Bài 5 - Số lượng số chẵn:", count_even_elements([1, 2, 3, 4]))