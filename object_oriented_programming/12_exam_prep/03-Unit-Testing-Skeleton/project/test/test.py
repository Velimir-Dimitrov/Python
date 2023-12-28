from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.test = SecondHandCar("test_model", "test_type", 100000, 100000.0)
        self.test2 = SecondHandCar("test_model2", "test_type2", 100000, 100000.0)

    def test_successful_initialization(self):
        self.assertEqual("test_model", self.test.model)
        self.assertEqual("test_type", self.test.car_type)
        self.assertEqual(100000.0, self.test.price)
        self.assertEqual(100000, self.test.mileage)
        self.assertEqual([], self.test.repairs)

    def test_setting_invalid_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.price = 1.0
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_setting_invalid_mileage_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_setting_invalid_promo_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.set_promotional_price(self.test.price)
        self.assertEqual('You are supposed to decrease the price!', str(ve.exception))

    def test_setting_valid_promo_price_changes_car_price(self):
        expected_return = 'The promotional price has been successfully set.'
        expected_price = 80000.0

        actual_return = self.test.set_promotional_price(80000.0)
        actual_price = self.test.price

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_price, actual_price)

    def test_invalid_repair_does_not_change_price_and_list_of_repairs(self):
        expected_repairs_list = []
        expected_price = 100000.0
        expected_return = 'Repair is impossible!'

        actual_return = self.test.need_repair(60000.0, "new engine")

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_price, self.test.price)
        self.assertEqual(expected_repairs_list, self.test.repairs)

    def test_successful_repair_changes_price_and_list_of_repairs(self):
        expected_repairs_list = ["new engine"]
        expected_price = 150000.0
        expected_return = f'Price has been increased due to repair charges.'

        actual_return = self.test.need_repair(50000.0, "new engine")

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_price, self.test.price)
        self.assertEqual(expected_repairs_list, self.test.repairs)

    def test_invalid_comparing_due_to_different_types_of_cars_return_message(self):
        expected_return = 'Cars cannot be compared. Type mismatch!'
        actual_return = self.test > self.test2

        self.assertEqual(expected_return, actual_return)

    def test_successful_comparing_between_same_type_of_cars_return_false_with_same_price_or_lower_price_for_first_car(self):
        self.test2.car_type = "test_type"

        expected_return = False
        actual_return = self.test > self.test2

        self.assertEqual(expected_return, actual_return)

        self.test2.car_type = "test_type"
        self.test2.price = 120000.0

        expected_return = False
        actual_return = self.test > self.test2

        self.assertEqual(expected_return, actual_return)

    def test_successful_comparing_between_same_type_of_cars_with_different_prices(self):
        self.test2.car_type = "test_type"
        self.test2.price = 60000.0

        expected_return = True
        actual_return = self.test > self.test2

        self.assertEqual(expected_return, actual_return)

    def test_string_return(self):
        expected_return = f"""Model {self.test.model} | Type {self.test.car_type} | Milage {self.test.mileage}km
Current price: {self.test.price:.2f} | Number of Repairs: {len(self.test.repairs)}"""
        actual_return = self.test.__str__()
        self.assertEqual(expected_return, actual_return)


if __name__ == "__main__":
    main()
