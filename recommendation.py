# AI Recommendation System - Movie Recommender
# AI Recommendation System - Movie Recommender

movies = {
    "Avengers": ["Action", "Sci-Fi"],
    "Iron Man": ["Action", "Sci-Fi"],
    "Captain America": ["Action", "Adventure"],
    "Thor": ["Action", "Fantasy"],
    "Spider-Man": ["Action", "Adventure"],
    "Black Panther": ["Action", "Adventure"],
    "Doctor Strange": ["Action", "Fantasy"],

    "Interstellar": ["Sci-Fi", "Adventure"],
    "Inception": ["Sci-Fi", "Action"],
    "The Matrix": ["Sci-Fi", "Action"],
    "Avatar": ["Sci-Fi", "Adventure"],
    "Dune": ["Sci-Fi", "Adventure"],
    "Gravity": ["Sci-Fi", "Drama"],

    "John Wick": ["Action", "Thriller"],
    "Mission Impossible": ["Action", "Thriller"],
    "Mad Max: Fury Road": ["Action", "Adventure"],
    "Top Gun: Maverick": ["Action", "Drama"],

    "The Hangover": ["Comedy"],
    "Superbad": ["Comedy"],
    "21 Jump Street": ["Comedy", "Action"],
    "Free Guy": ["Comedy", "Sci-Fi"],
    "Jumanji": ["Comedy", "Adventure"],

    "Toy Story": ["Animation", "Comedy"],
    "Frozen": ["Animation", "Family"],
    "Finding Nemo": ["Animation", "Family"],
    "The Lion King": ["Animation", "Drama"],
    "Shrek": ["Animation", "Comedy"],

    "Titanic": ["Romance", "Drama"],
    "The Notebook": ["Romance", "Drama"],
    "La La Land": ["Romance", "Drama"],
    "Pride and Prejudice": ["Romance", "Drama"],

    "The Dark Knight": ["Action", "Drama"],
    "Joker": ["Drama", "Thriller"],
    "Forrest Gump": ["Drama"],
    "The Shawshank Redemption": ["Drama"],
    "Fight Club": ["Drama", "Thriller"],

    "The Conjuring": ["Thriller"],
    "A Quiet Place": ["Thriller", "Sci-Fi"],
    "Get Out": ["Thriller"],
    "Bird Box": ["Thriller", "Drama"],

    "Harry Potter": ["Fantasy", "Adventure"],
    "The Lord of the Rings": ["Fantasy", "Adventure"],
    "The Hobbit": ["Fantasy", "Adventure"],
    "Pirates of the Caribbean": ["Adventure", "Fantasy"]
}

print("=" * 50)
print("      AI MOVIE RECOMMENDATION SYSTEM")
print("=" * 50)

print("\nAvailable Genres:")
print("Action, Sci-Fi, Comedy, Animation, Romance, Drama, Thriller, Adventure, Family, Fantasy")

user_input = input("\nEnter your favorite genres (separated by commas): ")

genres = [genre.strip() for genre in user_input.split(",")]

scores = {}

for movie, movie_genres in movies.items():
    score = 0

    for genre in genres:
        if genre in movie_genres:
            score += 1

    scores[movie] = score

sorted_movies = sorted(
    scores.items(),
    key=lambda item: item[1],
    reverse=True
)

print("\n" + "=" * 50)
print("           TOP RECOMMENDATIONS")
print("=" * 50)

found = False

for movie, score in sorted_movies:
    if score > 0:
        print(f"{movie:<30} Match Score: {score}")
        found = True

if not found:
    print("No matching movies found.")

print("\nThank you for using the AI Movie Recommendation System!")