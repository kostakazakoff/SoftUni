from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookstore(TestCase):
    def setUp(self) -> None:
        self.store = Bookstore(100)

    def test__initialising(self):
        self.assertEqual(100, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store.total_sold_books)

    def test__books_limit_setter__limit_less_or_equal_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0
        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test__len__(self):
        self.assertEqual(0, self.store.__len__())
        self.store.availability_in_store_by_book_titles = {'Book': 2, 'Book2': 2}
        self.assertEqual(4, len(self.store))

    def test__receive_book__over_limit(self):
        with self.assertRaises(Exception) as ex:
            self.store.receive_book('Book3', 101)

        self.assertEqual("Books limit is reached. Cannot receive more books!", str(ex.exception))

    def test__receive_book_result(self):
        self.store.availability_in_store_by_book_titles = {'Book': 2, 'Book2': 2}

        result = self.store.receive_book('Book', 3)
        self.assertEqual({'Book': 5, 'Book2': 2}, self.store.availability_in_store_by_book_titles)
        self.assertEqual("5 copies of Book are available in the bookstore.", result)

        result = self.store.receive_book('Book3', 3)
        self.assertEqual({'Book': 5, 'Book2': 2, 'Book3': 3}, self.store.availability_in_store_by_book_titles)
        self.assertEqual("3 copies of Book3 are available in the bookstore.", result)

    def test__sell_book__book_title_not_in(self):
        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Book', 1)

        self.assertEqual("Book Book doesn't exist!", str(ex.exception))

    def test__sell_book__not_enough_books(self):
        self.store.availability_in_store_by_book_titles = {'Book': 1, 'Book2': 2}

        with self.assertRaises(Exception) as ex:
            self.store.sell_book('Book', 3)

        self.assertEqual("Book has not enough copies to sell. Left: 1", str(ex.exception))

    def test__sell_book__result(self):
        self.store.availability_in_store_by_book_titles = {'Book': 3, 'Book2': 2}

        self.assertEqual("Sold 2 copies of Book", self.store.sell_book('Book', 2))
        self.assertEqual(2, self.store.total_sold_books)
        self.assertEqual({'Book': 1, 'Book2': 2}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(3, len(self.store))

        self.assertEqual("Sold 1 copies of Book", self.store.sell_book('Book', 1))
        self.assertEqual(3, self.store.total_sold_books)
        self.assertEqual({'Book': 0, 'Book2': 2}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(2, len(self.store))

    def test__str__(self):
        self.store.availability_in_store_by_book_titles = {'Book': 1, 'Book2': 2}
        self.store._Bookstore__total_sold_books = 20

        result = ["Total sold books: 20",
                  'Current availability: 3',
                  " - Book: 1 copies",
                  " - Book2: 2 copies"]
        result = '\n'.join(result)

        self.assertEqual(result, str(self.store))

    def test__str__no_books(self):
        self.store._Bookstore__total_sold_books = 20

        result = ["Total sold books: 20",
                  'Current availability: 0']
        result = '\n'.join(result)

        self.assertEqual(result, str(self.store))


if __name__ == '__main__':
    main()
