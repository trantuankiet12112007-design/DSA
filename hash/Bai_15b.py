import random

class MinHashSignature:
    def __init__(self, num_hashes=10):
        self.num_hashes = num_hashes
        self.salts = [random.randint(0, 100000) for _ in range(num_hashes)]

    def compute_signature(self, elements_set):
        signature = []
        for i in range(self.num_hashes):
            min_val = float('inf')
            for item in elements_set:
                val_hash = hash(f"{item}-{self.salts[i]}")
                if val_hash < min_val:
                    min_val = val_hash
            signature.append(min_val)
        return signature

def estimate_jaccard_similarity(sig1, sig2):
    matches = sum(1 for i, j in zip(sig1, sig2) if i == j)
    return matches / len(sig1)

mh = MinHashSignature(num_hashes=20)
set_1 = {"apple", "banana", "cherry"}
set_2 = {"banana", "cherry", "date"}

sig_1 = mh.compute_signature(set_1)
sig_2 = mh.compute_signature(set_2)
print(f"Bài 15 - Hệ số Jaccard ước lượng xấp xỉ: {estimate_jaccard_similarity(sig_1, sig_2):.2f}")