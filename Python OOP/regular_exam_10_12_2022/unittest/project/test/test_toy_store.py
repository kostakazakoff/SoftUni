from unittest import TestCase, main
from project.toy_store import ToyStore

class TestYoyStore(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test__initialising(self):
        result = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(result, self.store.toy_shelf)

    def test__add_toy(self):
        with self.assertRaises(Exception) as error:
            self.store.add_toy('H', 'Toy')
        self.assertEqual("Shelf doesn't exist!", str(error.exception))

        result = self.store.add_toy('A', 'ToyA')
        self.assertEqual('ToyA', self.store.toy_shelf['A'])
        self.assertEqual("Toy:ToyA placed successfully!", result)

        result = self.store.add_toy('B', 'ToyB')
        self.assertEqual('ToyB', self.store.toy_shelf['B'])
        self.assertEqual({
            "A": 'ToyA',
            "B": 'ToyB',
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)
        self.assertEqual("Toy:ToyB placed successfully!", result)

        with self.assertRaises(Exception) as error:
            self.store.add_toy('A', 'ToyA')
        self.assertEqual("Toy is already in shelf!", str(error.exception))

        with self.assertRaises(Exception) as error:
            self.store.add_toy('A', 'ToyX')
        self.assertEqual("Shelf is already taken!", str(error.exception))

    def test__remove_toy(self):
        self.store.add_toy('A', 'ToyA')
        self.store.add_toy('B', 'ToyB')
        result = self.store.remove_toy('B', 'ToyB')
        self.assertEqual(None, self.store.toy_shelf['B'])
        self.assertEqual({
            "A": 'ToyA',
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }, self.store.toy_shelf)
        self.assertEqual("Remove toy:ToyB successfully!", result)

        with self.assertRaises(Exception) as error:
            self.store.remove_toy('H', 'Toy')
        self.assertEqual("Shelf doesn't exist!", str(error.exception))

        with self.assertRaises(Exception) as error:
            self.store.remove_toy('A', 'Toy')
        self.assertEqual("Toy in that shelf doesn't exists!", str(error.exception))


if __name__ == '__main__':
    main()
