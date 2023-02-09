product = input()
q = int(input())


def order_cost(order, quantity):
    total = lambda x, y: x * y
    orders = {
        'coffee': 1.5,
        'coke': 1.4,
        'water': 1.0,
        'snacks': 2.0,
    }
    for key, value in orders.items():
        if key == order:
            price = value
    return total(quantity, price)


print(f'{order_cost(product, q):.2f}')
