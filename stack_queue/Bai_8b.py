class CustomDeque:
    def __init__(self):
        self.items = []

    def pushFront(self, x):
        self.items.insert(0, x)

    def pushBack(self, x):
        self.items.append(x)

    def popFront(self):
        if not self.items: raise IndexError("Deque rỗng.")
        return self.items.pop(0)

    def popBack(self):
        if not self.items: raise IndexError("Deque rỗng.")
        return self.items.pop()


dq = CustomDeque()
dq.pushFront(1); dq.pushBack(2)
print("Bài 8 - Mảng:", dq.items)