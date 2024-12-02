def grocery_store(**kwargs):
    output = ''
    ordered_products = dict(sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0])))
    for product_name, product_quantity in ordered_products.items():
        output += f'{product_name}: {product_quantity}\n'
    return output


print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))