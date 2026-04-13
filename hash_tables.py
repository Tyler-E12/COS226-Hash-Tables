# the hash table is using linear probing now
# each index stores a single item, collissions are handled by moving forward
class LinearProbingHashTable:
    def __init__(self, size, hash_function):
        self.size = size
        # no buckets just slots
        self.table = [None for _ in range(size)]
        self.hash_function = hash_function
        self.collisions = 0


    # this inserts a key value pair into the hash table and if multiple items map to the
    # same index then we move forward until an empty spot is found (collision detected)
    def insert(self, key, value):
        index = self.hash_function(key, self.size)
        start_index = index

        # counts the collisions (each occupied slot we pass is a collision)
        while self.table[index] is not None:
            self.collisions += 1
            index = (index + 1) % self.size

            if index == start_index:
                raise Exception("Hash table is full")

        self.table[index] = (key, value)


    # searches for a key in the hash table
    def search(self, key):
        index = self.hash_function(key, self.size)
        start_index = index

        # loop through table using probing to find key
        while self.table[index] is not None:
            k, v = self.table[index]
            if k == key:
                return v

            index = (index + 1) % self.size

            if index == start_index:
                break

        return None


    # counts to see how many slots went unused and are empty
    def wasted_space(self):
        empty_slots = self.table.count(None)
        return empty_slots
