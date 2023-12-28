from student import Student
from unittest import TestCase, main


class TestStudent(TestCase):

    def setUp(self):
        self.student = Student("Gosho")
        self.student2 = Student("Pesho", {"Python Fundamentals": ["Functions", "Lists"]})

    def test_initialization_with_no_courses(self):
        self.assertEqual("Gosho", self.student.name)
        self.assertIsInstance(self.student.courses, dict)

    def test_initialization_with_courses(self):
        self.assertEqual("Pesho", self.student2.name)
        self.assertEqual({"Python Fundamentals": ["Functions", "Lists"]}, self.student2.courses)

    def test_enroll_already_stored_course_and_update_notes(self):
        self.student.courses = {"Python OOP": ["Classes and Objectives"]}
        result = self.student.enroll("Python OOP", [ "Inheritance", "Encapsulation"], "")

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual({"Python OOP":
                              ["Classes and Objectives", "Inheritance", "Encapsulation"]}, self.student.courses)

    def test_enroll_missing_course_and_notes(self):

        result = self.student.enroll("Python Advanced", ["Stacks"], "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Python Advanced": ["Stacks"]}, self.student.courses)

        result = self.student.enroll("Python OOP", ["Testing"], "")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual({"Python Advanced": ["Stacks"], "Python OOP": ["Testing"]}, self.student.courses)

    def test_enroll_missing_course_without_adding_notes(self):
        result = self.student.enroll("Python Advanced", ["Stacks"], "n")

        self.assertEqual("Course has been added.", result)
        self.assertEqual({"Python Advanced": []}, self.student.courses)

    def test_successfully_adding_notes_to_existing_course(self):
        self.student.courses = {"Python Basics": ["For Loop"]}
        result = self.student.add_notes("Python Basics", "While Loop")
        self.assertEqual("Notes have been updated", result)
        self.assertEqual({"Python Basics": ["For Loop", "While Loop"]}, self.student.courses)

    def test_adding_note_to_missing_course_raises_exception_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Python Basics", "While Loop")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))
        self.assertEqual({}, self.student.courses)

    def test_successfully_leaving_course(self):
        self.student.courses = {"Python Basics": ["For Loop"]}
        result = self.student.leave_course("Python Basics")
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_leaving_course_that_does_not_exist_raises_exception_error(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Python Basics")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))
        self.assertEqual({}, self.student.courses)


if __name__ == "__main__":
    main()
