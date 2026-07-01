class ResizingArrayList:
    def __init__(self, initial_capacity=4):
        self.capacity = initial_capacity
        self.size = 0
        self.array = [None] * self.capacity

    def add(self, x):
        if self.size == self.capacity:
            self._resize()
        self.array[self.size] = x
        self.size += 1

    def _resize(self):
        self.capacity *= 2
        new_array = [None] * self.capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        print(f"[Resize] Dung lượng mới tăng lên: {self.capacity}")

r_arr = ResizingArrayList(initial_capacity=2)
r_arr.add(1); r_arr.add(2)
r_arr.add(3)