# I tweaked the prime around a bit and made it 37, it seems to have lowered the collisions
# by a decent amount.

# good hash function using polynomial rolling
def optimized_hash(key, size):
    hash_value = 0
    # updated this for a better spread
    prime = 37

    for char in key:
        hash_value = (hash_value * prime + ord(char)) % size

    return hash_value
