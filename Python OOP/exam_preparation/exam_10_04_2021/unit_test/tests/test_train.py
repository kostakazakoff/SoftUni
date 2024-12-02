from unittest import TestCase, main
from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train('Orient', 5)

    def test__initialising(self):
        self.assertEqual('Orient', self.train.name)
        self.assertEqual(5, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test__add__train_full(self):
        self.train.passengers = ['a', 'b', 'c', 'd', 'e']
        with self.assertRaises(ValueError) as error:
            self.train.add('f')
        self.assertEqual("Train is full", str(error.exception))

    def test__add__duplicated_passenger(self):
        self.train.passengers = ['a', 'b']
        with self.assertRaises(ValueError) as error:
            self.train.add('a')
        self.assertEqual("Passenger a Exists", str(error.exception))

    def test__add(self):
        self.train.passengers = ['a', 'b']
        self.train.add('c')
        self.assertEqual(['a', 'b', 'c'], self.train.passengers)

    def test__remove__no_such_passenger_in_train(self):
        self.train.passengers = ['a', 'b']
        with self.assertRaises(ValueError) as error:
            self.train.remove('c')
        self.assertEqual("Passenger Not Found", str(error.exception))

    def test__remove(self):
        self.train.passengers = ['a', 'b']
        self.train.remove('b')
        self.assertEqual(['a'], self.train.passengers)


if __name__ == '__main__':
    main()