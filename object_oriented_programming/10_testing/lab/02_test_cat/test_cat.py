from unittest import TestCase, main
from cat import Cat


class TestCat(TestCase):

    def setUp(self):
        self.cat = Cat("Tom")

    def test_feed_cat_expect_fed_and_sleepy_expect_size_increase(self):
        expected_size = 1
        self.cat.eat()
        self.assertEqual(expected_size, self.cat.size)
        self.assertTrue(self.cat.sleep)
        self.assertTrue(self.cat.fed)

    def test_feed_cat_while_fed_raises_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleep_while_cat_not_fed_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_not_sleepy_after_sleeping(self):
        self.cat.fed = True
        self.cat.sleepy = True
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == "__main__":
    main()
