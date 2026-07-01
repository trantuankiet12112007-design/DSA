class SimpleHashSet:
    def __init__(self):
        self.buckets = [[] for _ in range(16)]

    def _get_idx(self, key):
        return hash(key) % len(self.buckets)

    def add(self, key):
        idx = self._get_idx(key)
        if key not in self.buckets[idx]:
            self.buckets[idx].append(key)

    def contains(self, key):
        idx = self._get_idx(key)
        return key in self.buckets[idx]

    def remove(self, key):
        idx = self._get_idx(key)
        if key in self.buckets[idx]:
            self.buckets[idx].remove(key)

hs = SimpleHashSet()
hs.add(1); hs.add(1); hs.add(2)
print("Bài 11 - Tập hợp có chứa 1 không?:", hs.contains(1))