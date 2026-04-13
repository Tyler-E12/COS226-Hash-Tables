# this version of the hash function doesn't use key length for indexing like commit 1,
# it actually uses polynomials (based off of characters) IN the keys instead.
# this ends up greatly reducing the number of collisions.
# there's also barely any wasted space, but the build time is slightly longer.
def poly_hash(key, size):

    hash_value = 0
    prime = 31

    for char in key:
        hash_value = (hash_value * prime + ord(char)) % size

    return hash_value
