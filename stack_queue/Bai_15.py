def sort_stack(stack):
    temp_stack = []
    while stack:
        tmp = stack.pop()
        while temp_stack and temp_stack[-1] > tmp:
            stack.append(temp_stack.pop())
        temp_stack.append(tmp)

    while temp_stack:
        stack.append(temp_stack.pop())
    return stack


print("Bài 15:", sort_stack([3, 1, 2]))