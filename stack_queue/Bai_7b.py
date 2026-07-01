def reverse_queue(q_list):
    stack = []
    while q_list:
        stack.append(q_list.pop(0))
    while stack:
        q_list.append(stack.pop())
    return q_list

print("Bài 7:", reverse_queue([1, 2, 3]))