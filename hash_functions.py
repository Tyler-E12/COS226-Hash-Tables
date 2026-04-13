# the poor hash on purpose for the first commit
# this is bad on purpose because a bunch of different keys can have the same length
# which would cause a LOT of collisions

# key = the key thats being hashed
# size = the actual size of the hash table itself
def bad_hash(key, size):
    # returns the index in the hash table
    return len(key) % size