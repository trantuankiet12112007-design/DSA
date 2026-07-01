class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

ms = MinStack()
for v in [5, 3, 7]: ms.push(v)
print("Bài 7 - Min hiện tại:", ms.get_min())