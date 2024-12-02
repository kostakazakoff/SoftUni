from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart('Lidl', 100.0)
        self.cart2 = ShoppingCart('Market', 120.0)

    def test__initialising(self):
        self.assertEqual('Lidl', self.cart.shop_name)
        self.assertEqual(100.0, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test__shop_name_setter(self):
        for name in ['billa', '1lev']:
            with self.assertRaises(ValueError) as ve:
                self.cart.shop_name = name
            self.assertEqual("Shop must contain only letters and must "
                             "start with capital letter!",
                             str(ve.exception))

    def test__add_to_cart__product_price_more_equal_100(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart('water', 100)
        self.assertEqual("Product water cost too much!",
                         str(ve.exception))

    def test__add_to_cart(self):
        result = self.cart.add_to_cart('water', 2)
        self.assertEqual({'water': 2.00}, self.cart.products)
        self.assertEqual("water product was successfully added to the cart!", result)

    def test__remove_from_cart(self):
        self.cart.products = {'water': 2.00, 'banana': 3.0}

        result = self.cart.remove_from_cart('water')
        self.assertEqual({'banana': 3.0}, self.cart.products)
        self.assertEqual("Product water was successfully removed from the cart!", result)

        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart('water')
        self.assertEqual({'banana': 3.0}, self.cart.products)
        self.assertEqual("No product with name water in the cart!",
                         str(ve.exception))

    def test__add__(self):
        self.cart.products = {'a': 1.00, 'b': 1.00}
        self.cart2.products = {'c': 1.00, 'd': 1.00}

        result = self.cart.__add__(self.cart2)
        self.assertEqual(ShoppingCart, result.__class__)
        self.assertEqual({'a': 1.00, 'b': 1.00, 'c': 1.00, 'd': 1.00},
                         result.products)
        self.assertEqual('LidlMarket', result.shop_name)
        self.assertEqual(220.00, result.budget)

    def test__buy_products(self):
        self.cart.products = {'a': 60, 'b': 30}
        self.assertEqual('Products were successfully bought! Total cost: 90.00lv.',
                         self.cart.buy_products())
        self.cart.products = {'a': 60, 'b': 100}
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        self.assertEqual("Not enough money to buy the products! Over budget with 60.00lv!",
                         str(ve.exception))


if __name__ == '__main__':
    main()