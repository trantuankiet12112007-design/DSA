class EndOperationsList:
    def __init__(self):
        self.data = []

    def append(self, x):
        self.data.append(x)

    def pop_back(self):
        if not self.data:
            raise IndexError("Danh sách rỗng.")
        return self.data.pop()


arr = EndOperationsList()
arr.append(1); arr.append(2); arr.append(3)
print("Bài 2 - pop_back:", arr.pop_back())
print("Bài 2 - Danh sách sau pop:", arr.data)