# Define a list of movies with their genres

movies = [

{"title": "The Shawshank Redemption", "genres": ["Drama"]},

{"title": "The Dark Knight", "genres": ["Action", "Crime", "Drama"]},

{"title": "Inception", "genres": ["Action", "Adventure", "Sci-Fi"]},

{"title": "The Matrix", "genres": ["Action", "Sci-Fi"]},

{"title": "Forrest Gump", "genres": ["Drama", "Romance"]},

{"title": "The Godfather", "genres": ["Crime", "Drama"]},

{"title": "Titanic", "genres": ["Drama", "Romance"]},

{"title": "Interstellar", "genres": ["Adventure", "Drama", "Sci-Fi"]}

]

def recommend_movies(preferred_genres):

    """

    Recommends movies based on the user's preferred genres.

    

    Args:

    preferred_genres (list of str): List of genres the user prefers.

    

    Returns:

    list of str: List of movie titles that match the preferred genres.

    """

    recommended = []

    for movie in movies:

        # Check if any of the movie's genres match the user's preferred genres

        if any(genre in preferred_genres for genre in movie["genres"]):

            recommended.append(movie["title"])

    return recommended

def get_user_preferences():

    """

    Prompts the user to input their preferred genres.

    

    Returns:

    list of str: List of preferred genres input by the user.

    """

    print("Enter your preferred genres (comma-separated):")

    genres_input = input()

    preferred_genres = [genre.strip().capitalize() for genre in genres_input.split(",")]

    return preferred_genres

def main():

    """

    Main function to run the recommendation system.

    """

    print("Welcome to the Movie Recommendation System!")

    preferred_genres = get_user_preferences()

    recommendations = recommend_movies(preferred_genres)

    

    if recommendations:

        print("Based on your preferences, we recommend the following movies:")

        for movie in recommendations:

            print(f"- {movie}")

    else:

        print("Sorry, we couldn't find any movies matching your preferences.")

if __name__ == "__main__":

    main()
