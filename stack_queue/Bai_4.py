class FixedCapacityStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []

    def push(self, x):
        if len(self.stack) >= self.capacity:
            raise OverflowError("Stack Overflow: Ngăn xếp đã đầy.")
        self.stack.append(x)

    def pop(self):
        if not self.stack:
            raise IndexError("Stack Underflow: Ngăn xếp rỗng.")
        return self.stack.pop()

try:
    s = FixedCapacityStack(capacity=2)
    s.push(10)
    s.push(20)
    print("Bài 4 - Pop lần 1:", s.pop())  # Kết quả: 20
    print("Bài 4 - Pop lần 2:", s.pop())  # Kết quả: 10
except (OverflowError, IndexError) as e:
    print("Lỗi:", e)