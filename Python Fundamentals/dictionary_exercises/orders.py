class Order:
    def __init__(self, ordered_product, current_price, current_quantity):
        self._product = ordered_product
        self._price = float(current_price)
        self._quantity = int(current_quantity)
        self._order_price = self._price * self._quantity

    def add_new(self, new_price, new_quantity):
        self._quantity += int(new_quantity)
        self._price = float(new_price)
        self._order_price = self._price * self._quantity

    def output(self):
        return f'{self._product} -> {self._order_price:.2f}'


orders = dict()
product_parameters = input().split(' ')
while product_parameters[0] != 'buy':
    product, price, quantity = product_parameters
    if product not in orders:
        new_order = Order(product, price, quantity)
        orders[product] = new_order
    else:
        orders[product].add_new(price, quantity)
    product_parameters = input().split(' ')

for value in orders.values():
    print(value.output())
