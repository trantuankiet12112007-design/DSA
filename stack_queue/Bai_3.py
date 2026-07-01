def simulate_stack_operations(operations):
    stack = []
    for op in operations:
        if op.startswith("push"):
            val = int(op.split()[1])
            stack.append(val)
        elif op == "pop":
            if stack:
                print(f"Pop: {stack.pop()}")
            else:
                print("Pop lỗi: Stack rỗng")
    print(f"Trạng thái cuối cùng: {stack}")

print("Bài 3:")
simulate_stack_operations(["push 5", "push 7", "pop"])