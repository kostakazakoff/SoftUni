max_points = 0
best_movie = ''
for i in range(7):
    points = 0
    movie_points = 0
    name_of_the_movie = input()

    if name_of_the_movie == 'STOP':
        break

    for each in name_of_the_movie:
        points = ord(each)
        if each.islower():
            points -= 2 * len(name_of_the_movie)
        elif each.isupper():
            points -= len(name_of_the_movie)
        movie_points += points

    if movie_points > max_points:
        max_points = movie_points
        best_movie = name_of_the_movie

if i == 6 and name_of_the_movie != 'STOP':
    print('The limit is reached.')
print(f'The best movie for you is {best_movie} with {max_points} ASCII sum.')