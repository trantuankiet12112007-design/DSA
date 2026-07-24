class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity

    def append(self, val):
        if self.size == self.capacity:
            self.capacity *= 2
            new_arr = [None] * self.capacity
            for i in range(self.size):
                new_arr[i] = self.array[i]
            self.array = new_arr
        self.array[self.size] = val
        self.size += 1
