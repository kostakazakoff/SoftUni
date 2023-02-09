company_name = input()
nuber_of_adult_tickets = int(input())
number_of_kids_tickets = int(input())
net_price_adult = float(input())
tax = float(input())
net_price_kids = 0.3 * net_price_adult

profit = ((net_price_adult + tax) * nuber_of_adult_tickets + (net_price_kids + tax) * number_of_kids_tickets) * 0.2

print(f'The profit of your agency from {company_name} tickets is {profit:.2f} lv.')