class Catalogue:
    def __init__(self, name: str):
        self.name = name
        self.products = []

    def __repr__(self):
        output_products = "\n".join(sorted(self.products))
        output = f'Items in the {self.name} catalogue:\n{output_products}'
        return output

    def add_product(self, product_name: str):
        self.products.append(product_name)
        return self.products

    def get_by_letter(self, first_letter: str):
        output = [prod for prod in self.products if prod[0].lower() == first_letter.lower()]
        return output


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
