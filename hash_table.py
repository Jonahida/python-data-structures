class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Creating a list of empty lists

    def hash_function(self, key):
        return hash(key) % self.size  # Hash function to determine the index

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if key already exists in the index
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                print(f"Updated ({key}, {value}) at index {index}")
                return
        # No existing key found, insert new (key, value)
        self.table[index].append((key, value))
        print(f"Inserted ({key}, {value}) at index {index}")

    def search(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                print(f"Found: ({k}, {v}) at index {index}")
                return
        print(f"Key {key} not found.")

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                print(f"Deleted ({k}, {v}) from index {index}")
                return
        print(f"Key {key} not found.")

    def display(self):
        print("\nHash Table:")
        for index, bucket in enumerate(self.table):
            if bucket:  # Only display non-empty indices
                print(f"Index {index}: {bucket}")


