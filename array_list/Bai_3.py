class DynamicInsertDeleteList:
    def __init__(self):
        self.data = []

    def insert_at(self, index, x):
        self.data.append(None)
        for i in range(len(self.data) - 1, index, -1):
            self.data[i] = self.data[i - 1]
        self.data[index] = x

    def delete_at(self, index):
        if not (0 <= index < len(self.data)):
            raise IndexError("Chỉ số không hợp lệ.")
        res = self.data[index]

        for i in range(index, len(self.data) - 1):
            self.data[i] = self.data[i + 1]
        self.data.pop()
        return res

arr = DynamicInsertDeleteList()
arr.data = [1, 2, 4]
arr.insert_at(2, 3)
print("Bài 3 - Sau khi chèn 3 tại idx 2:", arr.data)