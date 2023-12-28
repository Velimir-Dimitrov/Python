from car_manager import Car
from unittest import TestCase, main


class TestCar(TestCase):

    def setUp(self):
        self.car = Car("BMW", "525", 10, 70)

    def test_successful_initialization(self):
        self.assertEqual("BMW", self.car.make)
        self.assertEqual("525", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(70, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_initializing_make_without_value_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_initializing_mode_without_value_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_initializing_no_fuel_consumption_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_initializing_no_fuel_capacity_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_setting_negative_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_receiving_positive_fuel_amount_and_refueling_successfully(self):
        expected_fuel_amount = 70
        self.car.refuel(80)
        self.assertEqual(expected_fuel_amount, self.car.fuel_amount)

    def test_receiving_no_fuel_and_failing_to_refuel_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_successfully_driving_valid_distance_with_sufficient_amount_of_fuel(self):
        self.car.fuel_amount = 35
        expected_fuel = 25
        self.car.drive(100)
        self.assertEqual(expected_fuel, self.car.fuel_amount)

    def test_no_sufficient_amount_of_fuel_to_drive_distance_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(50)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

if __name__ == "__main__":
    main()