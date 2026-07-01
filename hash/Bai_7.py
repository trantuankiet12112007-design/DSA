class RehashingHashTable:
    def __init__(self, capacity=4, load_factor_threshold=0.75):
        self.capacity = capacity
        self.threshold = load_factor_threshold
        self.size = 0
        self.table = [[] for _ in range(self.capacity)]

    def put(self, key, value):
        idx = hash(key) % self.capacity
        for item in self.table[idx]:
            if item[0] == key:
                item[1] = value
                return

        self.table[idx].append([key, value])
        self.size += 1

        if self.size / self.capacity > self.threshold:
            self._resize_and_rehash()

    def _resize_and_rehash(self):
        old_table = self.table
        self.capacity *= 2
        self.table = [[] for _ in range(self.capacity)]
        self.size = 0
        print(f"[Rehash] Mở rộng bảng lên dung lượng: {self.capacity}")

        for bucket in old_table:
            for key, value in bucket:
                self.put(key, value)

r_ht = RehashingHashTable(capacity=2)
r_ht.put('a', 1);
r_ht.put('b', 2)