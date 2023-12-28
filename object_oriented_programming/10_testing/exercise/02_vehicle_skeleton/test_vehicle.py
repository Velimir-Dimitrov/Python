from unittest import TestCase, main
from vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self):
        self.car = Vehicle(70.0, 200.0)

    def test_successful_initializing(self):
        self.assertEqual(70.0, self.car.fuel)
        self.assertEqual(200.0, self.car.horse_power)
        self.assertEqual(70, self.car.capacity)
        self.assertEqual(1.25, self.car.fuel_consumption)

    def test_type_of_inputs(self):
        self.assertIsInstance(self.car.fuel, float)
        self.assertIsInstance(self.car.horse_power, float)
        self.assertIsInstance(self.car.capacity, float)
        self.assertIsInstance(self.car.fuel_consumption, float)
        self.assertIsInstance(self.car.DEFAULT_FUEL_CONSUMPTION, float)

    def test_successfully_driving_particular_distance_with_sufficient_fuel(self):
        expected_fuel = 57.5
        self.car.drive(10)
        self.assertEqual(expected_fuel, self.car.fuel)

    def test_driving_raises_error_with_distance_and_insufficient_fuel(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_successfully_refueling_with_enough_fuel_to_not_pass_capacity(self):
        expected_fuel = 50
        self.car.fuel = 40
        self.car.refuel(10)
        self.assertEqual(expected_fuel, self.car.fuel)

    def test_refueling_with_too_much_fuel_passing_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(1000)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_successfully_using_str_method(self):
        expected_return = f"The vehicle has {self.car.horse_power} " \
               f"horse power with {self.car.fuel} fuel left and {self.car.fuel_consumption} fuel consumption"
        self.assertEqual(expected_return, str(self.car))


if __name__ == "__main__":
    main()