class LazyDeletionHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.DELETED = "TOMBSTONE_DELETED"

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        idx = self._hash(key)
        first_deleted_idx = -1
        start_idx = idx

        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            if self.keys[idx] == self.DELETED and first_deleted_idx == -1:
                first_deleted_idx = idx
            idx = (idx + 1) % self.capacity
            if idx == start_idx:
                break


        target_idx = first_deleted_idx if first_deleted_idx != -1 else idx
        self.keys[target_idx] = key
        self.values[target_idx] = value

    def remove(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.keys[idx] = self.DELETED
                self.values[idx] = None
                return True
            idx = (idx + 1) % self.capacity
            if idx == start_idx:
                break
        return False


lazy_ht = LazyDeletionHashTable()
lazy_ht.put('x', 50)
lazy_ht.remove('x')
print("Bài 14 - Trạng thái ô lưu của khoá 'x' sau xoá:", lazy_ht.keys[lazy_ht._hash('x')])