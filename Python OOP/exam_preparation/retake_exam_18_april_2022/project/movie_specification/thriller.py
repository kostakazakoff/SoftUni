from project.movie_specification.movie import Movie


class Thriller(Movie):
    genre_age_restriction = 16

    def __init__(self, title: str, year: int, owner: object, age_restriction: int = genre_age_restriction):
        super().__init__(title, year, owner, age_restriction)
