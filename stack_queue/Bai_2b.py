class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, x):
        if self.size == self.capacity:
            raise OverflowError("Hàng đợi vòng đã đầy.")
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError("Hàng đợi vòng rỗng.")
        res = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return res

cq = CircularQueue(capacity=4)
cq.enqueue(10); cq.enqueue(20)
print("Bài 2:", cq.dequeue())