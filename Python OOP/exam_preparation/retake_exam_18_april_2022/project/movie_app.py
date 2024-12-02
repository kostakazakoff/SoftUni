from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def __find_user(self, name):
        user = [u for u in self.users_collection if u.username == name]
        if user:
            return user[0]

    def register_user(self, username: str, age: int):
        if username in [u.username for u in self.users_collection]:
            raise Exception("User already exists!")
        self.users_collection.append(User(username, age))
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if not user:
            raise Exception("This user does not exist!")
        if user is not movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = self.__find_user(username)
        if user is not movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        [setattr(movie, attribute, value) for attribute, value in kwargs.items()]
        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        user = self.__find_user(username)
        if user is not movie.owner:
            raise Exception(f"{username} is not the owner of the movie {movie.title}!")
        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)
        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if user is movie.owner:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")
        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username: str, movie: Movie):
        user = self.__find_user(username)
        if movie not in user.movies_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        movie.likes -= 1
        user.movies_liked.remove(movie)
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        return '\n'.join(m.details() for m in sorted(self.movies_collection, key=lambda x: (-x.year, x.title)))

    def __str__(self):
        all_users = ', '.join(x.username for x in self.users_collection) if self.users_collection else 'No users.'
        all_movies = ', '.join(x.title for x in self.movies_collection) if self.movies_collection else 'No movies.'
        return f"All users: {all_users}\nAll movies: {all_movies}"
