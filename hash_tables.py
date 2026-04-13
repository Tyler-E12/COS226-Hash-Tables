# hashtable using linked list
# each of the indexes in the list stores a bucket
class LinkedListHashTable:
    def __init__(self, size, hash_function):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.hash_function = hash_function
        self.collisions = 0


    # this inserts a key-value pair into the hashtable and if muliple items map to the
    # same index then they are stored in the same bucket (collision detected)
    def insert(self, key, value):
        index = self.hash_function(key, self.size)
        bucket = self.table[index]

        # counts the collissions (traversing existing elements causes them)
        if bucket:
            self.collisions += len(bucket)

        bucket.append((key, value))

    # searches for a key in the hash table
    def search(self, key):
        index = self.hash_function(key, self.size)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v
        return None

    # counts to see how many buckets went unused and are empty
    def wasted_space(self):
        empty_buckets = sum(1 for bucket in self.table if len(bucket) == 0)
        return empty_buckets