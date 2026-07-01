class DoubleHashingHashTable:
    def __init__(self, capacity=11):
        self.capacity = capacity
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def _hash1(self, key):
        return hash(key) % self.capacity

    def _hash2(self, key):
        return 7 - (hash(key) % 7)

    def put(self, key, value):
        idx = self._hash1(key)
        step = self._hash2(key)
        start_idx = idx

        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            idx = (idx + step) % self.capacity
            if idx == start_idx:
                raise OverflowError("Bảng băm đầy!")

        self.keys[idx] = key
        self.values[idx] = value

dh_ht = DoubleHashingHashTable()
dh_ht.put('key1', "Value 1")
print("Bài 8 - Đã nạp thành công.")