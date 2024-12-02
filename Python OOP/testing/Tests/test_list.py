from unittest import TestCase, main
from List.extended_list import IntegerList


class IntegerListTest(TestCase):
    def setUp(self):
        self.int_list = IntegerList(1, 2, 3, 'A', 4.5, True)

    def test__initialising(self):
        self.assertEqual([1, 2, 3], self.int_list._IntegerList__data)

    def test__get_data(self):
        self.assertEqual([1, 2, 3], self.int_list.get_data())

    def test__add_method__raise_value_error(self):
        err_messages = []

        for el in [0.5, '1', True]:
            with self.assertRaises(ValueError) as ve:
                self.int_list.add(el)
            err_messages.append(str(ve.exception))

        for message in err_messages:
            self.assertEqual("Element is not Integer", message)

    def test__add__correct_output(self):
        result = self.int_list.add(1)
        self.assertEqual([1, 2, 3, 1], result)
        self.assertEqual([1, 2, 3, 1], self.int_list._IntegerList__data)

    # Code error -----------------------------------------------------
    def test_remove_index_expect_index_error(self):
        err_messages = []

        for idx in [-5, 3]:
            with self.assertRaises(IndexError)as ie:
                self.int_list.remove_index(idx)
            err_messages.append(str(ie.exception))

        for message in err_messages:
            self.assertEqual("Index is out of range", message)
    # -----------------------------------------------------------------

    def test__remove__index_output(self):
        result = self.int_list.remove_index(0)
        self.assertEqual(1, result)
        self.assertNotIn(1, self.int_list._IntegerList__data)

    # Code error -----------------------------------------------------
    def test__get__raise_index_error(self):
        err_messages = []

        for idx in [-5, 3]:
            with self.assertRaises(IndexError)as ie:
                self.int_list.get(idx)
            err_messages.append(str(ie.exception))

        for message in err_messages:
            self.assertEqual("Index is out of range", message)
    # -----------------------------------------------------------------

    def test__get__output(self):
        self.assertEqual(3, self.int_list.get(2))

    def test_insert__index_error_expect_out_of_range(self):
        with self.assertRaises(IndexError) as ie:
            self.int_list.insert(3, 5)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test__insert__value_error_expected_not_integer(self):
        err_messages = []

        for el in [0.5, '1', True]:
            with self.assertRaises(ValueError) as ve:
                self.int_list.insert(0, el)
            err_messages.append(str(ve.exception))

        for message in err_messages:
            self.assertEqual("Element is not Integer", message)

    def test__insert__output(self):
        self.int_list.insert(0, 5)
        self.assertIn(5, self.int_list._IntegerList__data)

    def test__get_biggest__(self):
        result = self.int_list.get_biggest()
        self.assertEqual(max(self.int_list._IntegerList__data), result)

    def test__get_index__(self):
        result = self.int_list.get_index(3)
        self.assertEqual(2, result)


if __name__ == '__main__':
    main()
