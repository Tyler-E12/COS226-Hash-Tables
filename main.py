# Tyler Edwards
# 4/8/26
# A program that collects data from a CSV file and creates two hash tables from it,
# using titles for one and quotes for the other. It then uses hash functions to map
# each key into an index in the tables. Lastly it lists things like collisions, wasted
# space, and build time.
import time
from data_load import load_movies
from hash_tables import LinearProbingHashTable
from hash_functions import good_hash

table_size = 20000

# this is the function that ACTUALLY builds the hash table with the movie information
def build_table(table, data, key_type):
    start = time.time()

    for movie in data:
        key = movie[key_type]
        table.insert(key, movie)

    end = time.time()
    return end - start

#prints the statistics for each of the hash tables
def print_stats(name, table, build_time):
    print(name)
    print(f"Collisions: {table.collisions}")
    print(f"Wasted Space: {table.wasted_space()}")
    print(f"Build Time: {build_time:.6f} seconds\n")


def main():
    movies = load_movies("MOCK_DATA.csv")

    # hash table 1 where the title is the key (with linear probing and good hash)
    title_table = LinearProbingHashTable(table_size, good_hash)
    time_title = build_table(title_table, movies, "title")
    print_stats("Title Key - Linear Probing (Good Linear Probing Hash)", title_table, time_title)

    # hash table 2 where the quote is the key (with linear probing and good hash)
    quote_table = LinearProbingHashTable(table_size, good_hash)
    time_quote = build_table(quote_table, movies, "quote")
    print_stats("Quote Key - Linear Probing (Good Linear Probing Hash)", quote_table, time_quote)

# what actually makes the program run
if __name__ == "__main__":
    main()
