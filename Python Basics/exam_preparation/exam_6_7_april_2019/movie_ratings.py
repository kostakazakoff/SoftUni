import sys
number_of_movies = int(input())
max_raiting = -sys.maxsize
min_raiting = sys.maxsize
max_raiting_movie = ''
min_raiting_movie = ''
raiting_sum = 0
for i in range(number_of_movies):
    name_of_the_movie = input()
    movie_rating = float(input())
    if movie_rating > max_raiting:
        max_raiting = movie_rating
        max_raiting_movie = name_of_the_movie
    if movie_rating < min_raiting:
        min_raiting = movie_rating
        min_raiting_movie = name_of_the_movie
    raiting_sum += movie_rating
average_raiting = raiting_sum / number_of_movies
print(f'{max_raiting_movie} is with highest rating: {max_raiting:.1f}')
print(f'{min_raiting_movie} is with lowest rating: {min_raiting:.1f}')
print(f'Average rating: {average_raiting:.1f}')