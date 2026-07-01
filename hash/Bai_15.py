import hashlib


class ConsistentHashingRing:
    def __init__(self, replicas=3):
        self.replicas = replicas
        self.ring = {}
        self.sorted_keys = []

    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode('utf-8')).hexdigest(), 16)

    def add_server(self, server: str):
        for i in range(self.replicas):
            virtual_node_key = f"{server}-node-{i}"
            val_hash = self._hash(virtual_node_key)
            self.ring[val_hash] = server
            self.sorted_keys.append(val_hash)
        self.sorted_keys.sort()

    def remove_server(self, server: str):
        for i in range(self.replicas):
            virtual_node_key = f"{server}-node-{i}"
            val_hash = self._hash(virtual_node_key)
            if val_hash in self.ring:
                del self.ring[val_hash]
                self.sorted_keys.remove(val_hash)

    def get_server(self, key: str) -> str:
        if not self.ring:
            return None
        val_hash = self._hash(key)

        for sk in self.sorted_keys:
            if val_hash <= sk:
                return self.ring[sk]
        return self.ring[self.sorted_keys[0]]


ch_ring = ConsistentHashingRing()
ch_ring.add_server("Server_A")
ch_ring.add_server("Server_B")
print("Bài 15 - Khoá 'data_1' được phân phối cấu hình vào:", ch_ring.get_server("data_1"))