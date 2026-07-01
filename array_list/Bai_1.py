class SimpleArrayList:
    def __init__(self):
        self.data = []

    def add(self, x):
        self.data.append(x)

    def get(self, index):
        if 0 <= index < len(self.data):
            return self.data[index]
        raise IndexError("Chỉ số nằm ngoài phạm vi.")

    def set(self, index, val):
        if 0 <= index < len(self.data):
            self.data[index] = val
        else:
            raise IndexError("Chỉ số nằm ngoài phạm vi.")

    def size(self):
        return len(self.data)


arr = SimpleArrayList()
arr.add(1); arr.add(2); arr.add(3)
print("Bài 1 - get(1):", arr.get(1))