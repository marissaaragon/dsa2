# Hash table to store package information
# Ideas from this YouTube video https://www.youtube.com/watch?v=9HFbhPscPU0
class HashTable:
    # Initialize hashtable with 10 initial capacity
    def __init__(self, initial_capacity=10):
        self.map = []
        for i in range(initial_capacity):
            self.map.append([])

    # Generates hash value for key value
    def _get_hash(self, key):
        return hash(key) % len(self.map)

    # Insert a key-value pair into the hash table
    def insert(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]
        bucket = self.map[key_hash]
        for pair in bucket:
            if pair[0] == key: # If key exists update value
                pair[1] = value
                return True
        bucket.append(key_value) # If key does not exist, add new pair
        return True

    # Insert a key-value pair into the hash table, lookup function
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Function to remove pair from the hash table
    def delete(self, key):
        key_hash = self._get_hash(key)

        if not self.map[key_hash]:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False

