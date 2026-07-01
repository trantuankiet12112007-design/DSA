def print_and_count_stack(stack):
    temp_stack = []
    count = 0

    while stack:
        val = stack.pop()
        print(val, end=" ")
        temp_stack.append(val)
        count += 1
    print()

    while temp_stack:
        stack.append(temp_stack.pop())

    return count


print("Bài 5:")
original_stack = [1, 2, 3]
print("Số phần tử:", print_and_count_stack(original_stack))