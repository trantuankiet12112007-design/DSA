class PolynomialRollingHash:
    def __init__(self, text: str, k: int, p: int = 31, m: int = 10**9 + 7):
        self.text = text
        self.k = k
        self.p = p
        self.m = m
        self.p_pow_k1 = pow(p, k - 1, m)

    def get_window_hashes(self):
        n = len(self.text)
        if n < self.k:
            return []

        hashes = []
        curr_hash = 0
        for i in range(self.k):
            val = ord(self.text[i]) - ord('a') + 1
            curr_hash = (curr_hash * self.p + val) % self.m
        hashes.append(curr_hash)

        for i in range(1, n - self.k + 1):
            old_val = ord(self.text[i - 1]) - ord('a') + 1
            curr_hash = (curr_hash - old_val * self.p_pow_k1) % self.m
            curr_hash = (curr_hash + self.m) % self.m

            new_val = ord(self.text[i + self.k - 1]) - ord('a') + 1
            curr_hash = (curr_hash * self.p + new_val) % self.m

            hashes.append(curr_hash)

        return hashes


prh = PolynomialRollingHash("abcde", 3)
print("Câu 47 So luong Hash cua cua so k=3:", len(prh.get_window_hashes()))
