from collections import deque

class StackUsingQueues:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x):
        self.q1.append(x)

    def pop(self):
        if not self.q1:
            raise IndexError("Pop từ ngăn xếp rỗng.")
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        res = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return res


sq = StackUsingQueues()
sq.push(10)
sq.push(20)
print("Bài 10 - Pop:", sq.pop())