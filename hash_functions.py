# brought back the bad hash so I can combine it with the linear probing
# linear probing + the bad hash caused an incredibly high amount of both collisions AND
# wasted space.
# the build time ended up around 11 seconds because I had to greatly increase the table
# size to even finish running the program without issue.

def bad_hash(key, size):
 
    return len(key) % size
