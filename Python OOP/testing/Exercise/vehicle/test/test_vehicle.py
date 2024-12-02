from unittest import TestCase, main
from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(50.5, 231.0)

    def test__initialising(self):
        self.assertEqual(50.5, self.vehicle.fuel)
        self.assertEqual(float, type(self.vehicle.fuel))
        self.assertEqual(231.0, self.vehicle.horse_power)
        self.assertEqual(float, type(self.vehicle.horse_power))
        self.assertEqual(50.5, self.vehicle.capacity)
        self.assertEqual(float, type(self.vehicle.capacity))
        self.assertEqual(1.25, self.vehicle.fuel_consumption)
        self.assertEqual(float, type(self.vehicle.DEFAULT_FUEL_CONSUMPTION))

    def test__drive__fuel_not_enough_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test__drive__fuel_decreasing_after_drive(self):
        self.vehicle.drive(10)
        self.assertEqual(38, self.vehicle.fuel)

    def test__refuel__more_than_capacity_expect_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(self.vehicle.capacity + 1)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test__refuel__increasing_fuel(self):
        self.vehicle.fuel = 10
        self.vehicle.refuel(10)
        self.assertEqual(20, self.vehicle.fuel)

    def test__str__return(self):
        expected = "The vehicle has 231.0 horse power with 50.5 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, self.vehicle.__str__())


if __name__ == '__main__':
    main()