name_of_the_movie = input()
hall_type = input()
number_of_tickets = int(input())
total = 0
if hall_type == 'normal':
    if name_of_the_movie == 'A Star Is Born':
        price_of_the_ticket = 7.5
    elif name_of_the_movie == 'Bohemian Rhapsody':
        price_of_the_ticket = 7.35
    elif name_of_the_movie == 'Green Book':
        price_of_the_ticket = 8.15
    elif name_of_the_movie == 'The Favourite':
        price_of_the_ticket = 8.75
elif hall_type == 'luxury':
    if name_of_the_movie == 'A Star Is Born':
        price_of_the_ticket = 10.5
    elif name_of_the_movie == 'Bohemian Rhapsody':
        price_of_the_ticket = 9.45
    elif name_of_the_movie == 'Green Book':
        price_of_the_ticket = 10.25
    elif name_of_the_movie == 'The Favourite':
        price_of_the_ticket = 11.55
elif hall_type == 'ultra luxury':
    if name_of_the_movie == 'A Star Is Born':
        price_of_the_ticket = 13.5
    elif name_of_the_movie == 'Bohemian Rhapsody':
        price_of_the_ticket = 12.75
    elif name_of_the_movie == 'Green Book':
        price_of_the_ticket = 13.25
    elif name_of_the_movie == 'The Favourite':
        price_of_the_ticket = 13.95
total = number_of_tickets * price_of_the_ticket
print(f'{name_of_the_movie} -> {total:.2f} lv.')