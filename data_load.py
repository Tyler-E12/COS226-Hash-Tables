import csv

# loads the movie data from a CSV file to be used later in the hash tables
def load_movies(filename):
    movies = []

    # this opens the CSV file
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # loops through each of the rows in the CSV file
        for row in reader:
            # this gets the title and quote while removing extra whitespace
            # (this means stuff like spaces before or after a keyword would make it recognized
            # as a different key)
            title = row['movie_title'].strip()
            quote = row['quote'].strip()

            # this handles empty fields
            if title and quote:
                movies.append({
                    "title": title,
                    "quote": quote
                })

    return movies