class MonitoredQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def enqueue(self, x):
        if len(self.queue) >= self.capacity:
            raise OverflowError("Hàng đợi đã đầy (Overflow).")
        self.queue.append(x)

    def dequeue(self):
        if not self.queue:
            raise IndexError("Hàng đợi rỗng (Underflow).")
        return self.queue.pop(0)

    def get_size(self):
        return len(self.queue)


try:
    mq = MonitoredQueue(capacity=2)
    mq.enqueue(100); mq.enqueue(200)
    print("Bài 4 - Kích thước:", mq.get_size())
except OverflowError as e:
    print("Lỗi:", e)