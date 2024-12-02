name_of_the_movie = input()
days = int(input())
tickets = int(input())
ticket_price = float(input())
tax = int(input())

total = days * tickets * ticket_price
profit = total - total * tax / 100

print(f'The profit from the movie {name_of_the_movie} is {profit:.2f} lv.')