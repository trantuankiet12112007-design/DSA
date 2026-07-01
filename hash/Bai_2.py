class LinearProbingHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        idx = self._hash(key)
        start_idx = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            idx = (idx + 1) % self.capacity
            if idx == start_idx:
                raise OverflowError("Bảng băm đã đầy!")
        self.keys[idx] = key
        self.values[idx] = value

    def get(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.capacity
            if idx == start_idx:
                break
        return None

lp_ht = LinearProbingHashTable()
lp_ht.put('a', 100)
print("Bài 2 - get('a'):", lp_ht.get('a'))