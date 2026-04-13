# I had to make the table size 20,000 from 10,000 before it would fully run the program
# but once it was able to run, there were far less collisions than previously. It was also
# much faster even though the size was much bigger.

# good hash function using polynomial rolling
def good_hash(key, size):
    hash_value = 0
    prime = 31

    for char in key:
        hash_value = (hash_value * prime + ord(char)) % size

    return hash_value
