from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):

    def setUp(self):
        self.test = Trip(10000.0, 2, True)

    def test_successful_initialization(self):
        self.assertEqual(10000.0, self.test.budget)
        self.assertEqual(2, self.test.travelers)
        self.assertIsInstance(self.test.is_family, bool)
        self.assertIsInstance(self.test.booked_destinations_paid_amounts, dict)

    def test_travelers_less_than_one_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            Trip(10, 0, True)
        self.assertEqual('At least one traveler is required!', str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            Trip(10, -1, True)
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_travelers_are_not_family(self):
        self.test = Trip(10000.0, 1, True)
        self.assertEqual(False, self.test.is_family)

        self.test = Trip(10000.0, 5, False)
        self.assertEqual(False, self.test.is_family)

    def test_invalid_destination_trip_returns_message(self):
        invalid_destination = "Turkey"
        expected_result = 'This destination is not in our offers, please choose a new one!'
        actual_result = self.test.book_a_trip(invalid_destination)
        self.assertEqual(expected_result, actual_result)

    def test_valid_destination_wit_insufficient_budget(self):
        expected_result = 'Your budget is not enough!'
        actual_result = self.test.book_a_trip("Australia")
        self.assertEqual(expected_result, actual_result)

    def test_successfully_booking_for_family_with_ten_percent_discount(self):
        expected_budget = 9100.00
        expected_return = 'Successfully booked destination Bulgaria! Your budget left is 9100.00'
        expected_dictionary = {"Bulgaria": 900}

        actual_return = self.test.book_a_trip("Bulgaria")
        actual_budget = self.test.budget
        actual_dictionary = self.test.booked_destinations_paid_amounts

        self.assertEqual(expected_budget, actual_budget)
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_dictionary, actual_dictionary)

    def test_successfully_booking_for_non_family(self):
        self.test_non_family = Trip(200000, 4, False)
        expected_budget = 175200.00
        expected_return = 'Successfully booked destination Brazil! Your budget left is 175200.00'
        expected_dictionary = {"Brazil": 24800}

        actual_return = self.test_non_family.book_a_trip("Brazil")
        actual_budget = self.test_non_family.budget
        actual_dictionary = self.test_non_family.booked_destinations_paid_amounts

        self.assertEqual(expected_budget, actual_budget)
        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_dictionary, actual_dictionary)

    def test_no_booking_status(self):
        expected_return = f'No bookings yet. Budget: {self.test.budget:.2f}'
        actual_return = self.test.booking_status()
        self.assertEqual(expected_return, actual_return)

    def test_existing_booked_destinations(self):
        self.test.booked_destinations_paid_amounts = {"New Zealand": 15000, "Bulgaria": 1000,}
        expected_return = ("Booked Destination: Bulgaria\nPaid Amount: 1000.00\n"
                           "Booked Destination: New Zealand\nPaid Amount: 15000.00\n"
                           "Number of Travelers: 2\nBudget Left: 10000.00")
        actual_return = self.test.booking_status()
        self.assertEqual(expected_return, actual_return)


if __name__ == "__main__":
    main()

