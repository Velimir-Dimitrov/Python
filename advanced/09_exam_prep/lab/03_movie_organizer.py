def movie_organizer(*collection):
    movie_dict = {}
    for movie_and_genre in collection:
        movie, genre = movie_and_genre
        if genre not in movie_dict:
            movie_dict[genre] = []
        movie_dict[genre].append(movie)
    result = ''
    for genre_movies in sorted(movie_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        genre, movies_list = genre_movies
        result += f"{genre} - {len(movies_list)}\n"
        for movie_name in sorted(movies_list):
            result += f"* {movie_name}\n"
    return result







print(movie_organizer(("The Matrix", "Sci-fi")))
print(movie_organizer(("The Godfather", "Drama"),
("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))

