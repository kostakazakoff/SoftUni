from unittest import TestCase, main
from car_manager.car_manager import Car


class TestCar(TestCase):

    def setUp(self):
        self.car = Car('Volvo', 'V50', 10, 60)

    def test__initialising(self):
        self.assertEqual('Volvo', self.car.make)
        self.assertEqual('V50', self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test__make_is_empty_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test__model_is_empty_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test__fuel_consumption_is_zero_or_less_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test__fuel_capacity_is_zero_or_less_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test__fuel_amount_is_less_than_zero_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test__refuel__fuel_input_less_than_zero_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test__refuel__more_than_capacity_expect_amount_equal_capacity(self):
        self.car.refuel(self.car.fuel_capacity + 1)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test__drive__needed_more_than_amount_expect_exception(self):
        self.car.fuel_amount = 2
        with self.assertRaises(Exception) as ex:
            self.car.drive(50)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test__drive__fuel_amount_decreasing(self):
        self.car.fuel_amount = 50
        self.car.drive(100)
        self.assertEqual(40, self.car.fuel_amount)


if __name__ == '__main__':
    main()
