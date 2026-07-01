class BloomFilter:
    def __init__(self, size=100, num_hashes=3):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * self.size

    def _get_hashes(self, item):
        indices = []
        for i in range(self.num_hashes):
            idx = hash(f"{item}-salt-{i}") % self.size
            indices.append(idx)
        return indices

    def add(self, item):
        for idx in self._get_hashes(item):
            self.bit_array[idx] = 1

    def contains(self, item):
        return all(self.bit_array[idx] == 1 for idx in self._get_hashes(item))

bf = BloomFilter()
bf.add("test_data")
print("Bài 14 - Chắc chắn không có 'stranger'?:", bf.contains("stranger"))