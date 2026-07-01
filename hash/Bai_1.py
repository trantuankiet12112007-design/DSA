class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class ChainingHashTable:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * self.capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        idx = self._hash(key)
        if not self.table[idx]:
            self.table[idx] = Node(key, value)
            return
        curr = self.table[idx]
        while curr:
            if curr.key == key:
                curr.value = value
                return
            if not curr.next:
                curr.next = Node(key, value)
                return
            curr = curr.next

    def get(self, key):
        idx = self._hash(key)
        curr = self.table[idx]
        while curr:
            if curr.key == key:
                return curr.value
            curr = curr.next
        return None

    def remove(self, key):
        idx = self._hash(key)
        curr = self.table[idx]
        prev = None
        while curr:
            if curr.key == key:
                if prev:
                    prev.next = curr.next
                else:
                    self.table[idx] = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

ht = ChainingHashTable()
ht.put('a', 1)
print("Bài 1 - get('a'):", ht.get('a'))