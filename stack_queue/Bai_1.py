class ArrayStack:
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Underflow: Không thể pop từ ngăn xếp rỗng.")
        return self.stack.pop()

    def top(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

s = ArrayStack()
s.push(1); s.push(2); s.push(3)
print("Bài 1:", s.pop())