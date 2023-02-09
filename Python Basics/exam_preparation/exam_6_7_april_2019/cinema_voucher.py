voucher = int(input())
purchase_type = input()
movie_tickets = 0
movie_tickets_price = 0
others = 0
others_price = 0
it_is_movie = False
it_is_other_purchase = False
while purchase_type != 'End':
    if len(purchase_type) > 8:
        it_is_movie = True
        movie_tickets_price += ord(purchase_type[0]) + ord(purchase_type[1])
    else:
        it_is_other_purchase = True
        others_price += ord(purchase_type[0])
    if movie_tickets_price > voucher or others_price > voucher:
        break
    if it_is_movie:
        voucher -= movie_tickets_price
        movie_tickets += 1
    elif it_is_other_purchase:
        voucher -= others_price
        others += 1
    movie_tickets_price = 0
    others_price = 0
    it_is_movie = False
    it_is_other_purchase = False
    purchase_type = input()
print(movie_tickets)
print(others)