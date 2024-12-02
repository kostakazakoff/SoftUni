from unittest import TestCase, main
from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory('Paint', 10)

    def test__initialising(self):
        self.assertEqual('Paint', self.factory.name)
        self.assertEqual(10, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)

    def test__add_ingredient__product_not_in_valid_ingredients(self):
        with self.assertRaises(TypeError) as error:
            self.factory.add_ingredient('invalid', 1)
        self.assertEqual("Ingredient of type invalid not allowed in PaintFactory", str(error.exception))

    def test__add_ingredient__product_cant_add(self):
        with self.assertRaises(ValueError) as error:
            self.factory.add_ingredient('white', 1000)
        self.assertEqual("Not enough space in factory", str(error.exception))

    def test__add_ingredient(self):
        self.factory.add_ingredient('red', 2)
        self.assertEqual({'red': 2}, self.factory.ingredients)
        self.factory.add_ingredient('red', 3)
        self.assertEqual({'red': 5}, self.factory.ingredients)
        self.factory.add_ingredient('white', 2)
        self.assertEqual({'red': 5, 'white': 2}, self.factory.ingredients)

    def test__remove_ingredient__product_not_in_factory(self):
        self.factory.add_ingredient('white', 2)
        with self.assertRaises(KeyError) as error:
            self.factory.remove_ingredient('red', 2)
        self.assertEqual("'No such ingredient in the factory'", str(error.exception))

    def test__remove_ingredient__invalid_quantity(self):
        self.factory.add_ingredient('white', 2)
        with self.assertRaises(ValueError) as error:
            self.factory.remove_ingredient('white', 10)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(error.exception))

    def test__remove_ingredient(self):
        self.factory.add_ingredient('white', 2)
        self.factory.add_ingredient('red', 2)
        self.factory.remove_ingredient('red', 1)
        self.assertEqual(1, self.factory.ingredients['red'])
        self.assertEqual({'white': 2, 'red': 1}, self.factory.ingredients)

    def test__products(self):
        self.factory.add_ingredient('white', 2)
        self.assertEqual({'white': 2}, self.factory.products)


if __name__ == '__main__':
    main()