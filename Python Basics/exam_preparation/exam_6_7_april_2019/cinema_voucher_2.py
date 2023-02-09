voucher = int(input())
purchase_type = input()
movie_tickets = 0
movie_tickets_price = 0
others = 0
others_price = 0

while purchase_type != 'End':
    if len(purchase_type) > 8:
        movie_tickets_price += ord(purchase_type[0]) + ord(purchase_type[1])
    else:
        others_price += ord(purchase_type[0])
    if 0 < movie_tickets_price <= voucher:
        movie_tickets += 1
        voucher -= movie_tickets_price
    elif 0 < others_price <= voucher:
        others += 1
        voucher -= others_price
    else:
        break
    movie_tickets_price = 0
    others_price = 0
    purchase_type = input()
print(movie_tickets)
print(others)