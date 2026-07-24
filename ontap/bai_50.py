class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def _hashes(self, item):
        hashes = []
        for i in range(self.num_hashes):
            hashes.append(hash((item, i)) % self.size)
        return hashes

    def add(self, item):
        for h in self._hashes(item):
            self.bit_array[h] = 1

    def contains(self, item):
        for h in self._hashes(item):
            if self.bit_array[h] == 0:
                return False
        return True

bf = BloomFilter(100, 3)
bf.add("apple")
print("Câu 50 contains('apple'):", bf.contains("apple"))
print("Câu 50 contains('banana'):", bf.contains("banana"))
