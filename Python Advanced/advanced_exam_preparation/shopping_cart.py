def shopping_cart(*args):
    cart = {'Dessert': [], 'Pizza': [], 'Soup': []}
    limit = {'Dessert': 2, 'Pizza': 4, 'Soup': 3}
    output = ''

    for meal in args:
        if meal == 'Stop': break
        product, products_quantity, products_limit = meal[1], len(cart[meal[0]]), limit[meal[0]]
        if products_quantity < products_limit and product not in cart[meal[0]]:
            cart[meal[0]].append(meal[1])

    if sum(len(x) for x in cart.values()) == 0:
        return 'No products in the cart!'

    for meal, products in dict(sorted(cart.items(), key=lambda x: (-len(x[1]), x[0]))).items():
        output += f'{meal}:\n'
        if products:
            products = ' - ' + '\n - '.join(sorted(products))
            output += f'{products}\n'
    
    return output


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))