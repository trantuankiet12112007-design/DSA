class CircularQueue:
    def __init__(self, k: int):
        self.queue = [None] * k
        self.capacity = k
        self.head = self.tail = -1

    def enqueue(self, val: int) -> bool:
        if (self.tail + 1) % self.capacity == self.head:
            return False  # Đầy
        if self.head == -1:
            self.head = 0
        self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = val
        return True

    def dequeue(self) -> bool:
        if self.head == -1:
            return False  # Rỗng
        if self.head == self.tail:
            self.head = self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        return True
