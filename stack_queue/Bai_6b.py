class QueueUsingStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, x):
        self.in_stack.append(x)

    def dequeue(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
        if not self.out_stack:
            raise IndexError("Dequeue từ hàng đợi rỗng.")
        return self.out_stack.pop()

qs = QueueUsingStacks()
qs.enqueue(10); qs.enqueue(20)
print("Bài 6:", qs.dequeue())