from project.product import Product


class ProductRepository:
    products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        try:
            target_product = next(filter(lambda p: p.name == product_name, self.products))
            return target_product
        except StopIteration:
            pass

    def remove(self, product_name):
        target_product = self.find(product_name)
        if target_product:
            self.products.remove(target_product)

    def __repr__(self):
        return '\n'.join([f'{product.name}: {product.quantity}' for product in self.products])