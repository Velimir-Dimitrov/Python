from unittest import TestCase, main
from project.railway_station import RailwayStation
from collections import deque


class TestRailwayStation(TestCase):

    def setUp(self):
        self.test = RailwayStation("Test")

    def test_initialization(self):
        self.assertEqual("Test", self.test.name)
        self.assertEqual(deque(), self.test.arrival_trains)
        self.assertEqual(deque(), self.test.departure_trains)

    def test_short_name_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.test.name = "asd"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

        with self.assertRaises(ValueError) as ve:
            self.test.name = ""
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_adding_arrival_train_to_deque(self):
        expected_deque = deque(["Test train"])
        self.test.new_arrival_on_board("Test train")
        self.assertEqual(expected_deque, self.test.arrival_trains)

    def test_arriving_train_is_different(self):
        self.test.arrival_trains = deque(["Test train", "Test train2"])
        expected_arrival_deque = deque(["Test train", "Test train2"])
        expected_departure_deque = deque()
        expected_return = f"There are other trains to arrive before Test Train2."

        actual_return = self.test.train_has_arrived("Test Train2")

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_arrival_deque, self.test.arrival_trains)
        self.assertEqual(expected_departure_deque, self.test.departure_trains)

    def test_arriving_train_is_the_correct_one_changes_arrivals_and_departure(self):
        self.test.arrival_trains = deque(["Test train", "Test train2"])
        expected_arrival_deque = deque(["Test train2"])
        expected_departure_deque = deque(["Test train"])
        expected_return = "Test train is on the platform and will leave in 5 minutes."

        actual_return = self.test.train_has_arrived("Test train")

        self.assertEqual(expected_return, actual_return)
        self.assertEqual(expected_arrival_deque, self.test.arrival_trains)
        self.assertEqual(expected_departure_deque, self.test.departure_trains)

    def test_train_leaving_successfully_and_returns_true(self):
        self.test.departure_trains = deque(["Test Train", "Test Train2"])
        expected_departure_deque = deque(["Test Train2"])
        expected_return = True

        actual_return = self.test.train_has_left("Test Train")

        self.assertEqual(expected_departure_deque, self.test.departure_trains)
        self.assertEqual(expected_return, actual_return)

    def test_train_fails_to_leave_and_returns_false(self):
        self.test.departure_trains = deque(["Test Train", "Test Train2"])
        expected_departure_deque = deque(["Test Train", "Test Train2"])
        expected_return = False

        actual_return = self.test.train_has_left("Test Train2")
        self.assertEqual(expected_departure_deque, self.test.departure_trains)
        self.assertEqual(expected_return, actual_return)


if __name__ == "__main__":
    main()