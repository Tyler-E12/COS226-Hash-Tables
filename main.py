# Tyler Edwards
# 4/8/26
# A program that collects data from a CSV file and creates two hash tables from it,
# using titles for one and quotes for the other. It then uses hash functions to map
# each key into an index in the tables. Lastly it lists things like collisions, wasted
# space, and build time.
import time
from data_load import load_movies
from hash_tables import LinkedListHashTable
from hash_functions import bad_hash

table_size = 2000


# this is the function that ACTUALLY builds the hash table with the movie information
def build_table(table, data, key_type):
    start_time = time.time()

    for movie in data:
        key = movie[key_type]
        table.insert(key, movie)

    end_time = time.time()
    return end_time - start_time


#prints the statistics for each of the hash tables
def print_stats(name, table, build_time):
    print(name)
    print(f"Collisions: {table.collisions}")
    print(f"Wasted Space: {table.wasted_space()}")
    print(f"Build Time: {build_time:.6f} seconds")
    print()  # just a blank line to separate the two tables information



def main():
    #loads the movie data from the file
    movies = load_movies("MOCK_DATA.csv")

    # hash table 1 where the title is the key
    title_table = LinkedListHashTable(table_size, bad_hash)
    time_title = build_table(title_table, movies, "title")
    print_stats("Hash Table 1 (Title Key - Bad Hash)", title_table, time_title)

    # hash table 2 where the quote is the key
    quote_table = LinkedListHashTable(table_size, bad_hash)
    time_quote = build_table(quote_table, movies, "quote")
    print_stats("Hash Table 2 (Quote Key - Bad Hash)", quote_table, time_quote)

# what actually makes the program run
if __name__ == "__main__":
    main()