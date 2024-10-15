class HashTable:
    def __init__(self, initial_capacity=10):
        self.map = []
        for i in range(initial_capacity):
            self.map.append([])

    def _get_hash(self, key):
        return hash(key) % len(self.map)

    def insert(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        bucket = self.map[key_hash]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return True
        bucket.append(key_value)
        return True

    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self._get_hash(key)

        if not self.map[key_hash]:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False









