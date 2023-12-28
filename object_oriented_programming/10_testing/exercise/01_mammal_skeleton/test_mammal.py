from mammal import Mammal
from unittest import TestCase, main


class TestMammal(TestCase):

    def setUp(self):
        self.cow = Mammal('Sivushka', "Bovine", "Moo")

    def test_successful_initialization(self):
        self.assertEqual("Sivushka", self.cow.name)
        self.assertEqual("Bovine", self.cow.type)
        self.assertEqual("Moo", self.cow.sound)
        self.assertEqual("animals", self.cow._Mammal__kingdom)

    def test_successfully_returning_string_with_animal_sound(self):
        expected_string = f"{self.cow.name} makes {self.cow.sound}"
        actual_result = self.cow.make_sound()
        self.assertEqual(expected_string, actual_result)

    def test_successfully_getting_the_animal_kingdom_string(self):
        expected_result = self.cow._Mammal__kingdom
        actual_result = self.cow.get_kingdom()
        self.assertEqual(expected_result, actual_result)

    def test_getting_info_string(self):
        expected_string = f"{self.cow.name} is of type {self.cow.type}"
        actual_result = self.cow.info()
        self.assertEqual(expected_string, actual_result)


if __name__ == "__main__":
    main()