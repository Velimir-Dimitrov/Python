from extended_list import IntegerList
from unittest import TestCase, main


class TestExtendedList(TestCase):

    def setUp(self):
        self.integer_list = IntegerList(0, 'a', 1, 0.5, 2, True, 3)

    def test_list_initialization(self):
        self.assertEqual([0, 1, 2, 3], self.integer_list.get_data())

    def test_successfully_adding_integer_element_to_integer_list(self):
        expected_list = self.integer_list.get_data() + [4]
        self.integer_list.add(4)
        self.assertEqual(expected_list, self.integer_list.get_data())

    def test_adding_non_integer_element_to_integer_list_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add('hi')
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_successfully_removing_index_from_integer_list(self):
        expected_list = self.integer_list.get_data()[1:]
        self.integer_list.remove_index(0)
        self.assertEqual(expected_list, self.integer_list.get_data())

    def test_removing_out_of_range_index_from_integer_list(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(len(self.integer_list.get_data()))
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_successfully_getting_specific_element_on_particular_index_in_integer_list(self):
        expected_element = 2
        self.integer_list.get(2)
        self.assertEqual(expected_element, self.integer_list.get_data()[2])

    def test_getting_index_out_of_range_in_integer_list_raises_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(len(self.integer_list.get_data()))
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_successfully_inserting_integer_element_on_valid_index_in_integer_list(self):
        expected_result = [0, 1, 4, 2, 3]
        self.integer_list.insert(2, 4)
        self.assertEqual(expected_result, self.integer_list.get_data())

    def test_inserting_particular_element_on_invalid_index_in_integer_list(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(len(self.integer_list.get_data()), 5)
        self.assertEqual("Index is out of range", str(ie.exception))

    def test_inserting_non_integer_element_on_valid_index_in_integer_list(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(0, 'y')
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_getting_biggest_number_in_integer_list(self):
        expected_number = 3
        actual_result = self.integer_list.get_biggest()
        self.assertEqual(expected_number, actual_result)

    def test_successful_get_index_element_in_list(self):
        expected_index = 3
        result = self.integer_list.get_index(3)
        self.assertEqual(expected_index, result)


if __name__ == "__main__":
    main()
