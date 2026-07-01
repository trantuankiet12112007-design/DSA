class SimplePriorityQueue:
    def __init__(self):
        self.queue = []

    def push(self, x):
        self.queue.append(x)
        self.queue.sort(reverse=True)

    def pop(self):
        if not self.queue:
            raise IndexError("Hàng đợi ưu tiên rỗng.")
        return self.queue.pop()


pq = SimplePriorityQueue()
pq.push(30); pq.push(10); pq.push(20)
print("Bài 10:", pq.pop())