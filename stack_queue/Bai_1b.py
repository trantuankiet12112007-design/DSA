class BaseQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, x):
        self.queue.append(x)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow: Hàng đợi rỗng.")
        return self.queue.pop(0)

    def front(self):
        return self.queue[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.queue) == 0


q = BaseQueue()
q.enqueue(1); q.enqueue(2); q.enqueue(3)
print("Bài 1:", q.dequeue())