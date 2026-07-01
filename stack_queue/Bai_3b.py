def simulate_queue_operations(operations):
    queue = []
    for op in operations:
        if op.startswith("enq"):
            val = int(op.split()[1])
            queue.append(val)
        elif op == "deq":
            if queue:
                print(f"Dequeue: {queue.pop(0)}")
            else:
                print("Dequeue lỗi: Hàng đợi rỗng")
    print(f"Trạng thái cuối cùng: {queue}")

print("Bài 3:")
simulate_queue_operations(["enq 5", "enq 7", "deq"])