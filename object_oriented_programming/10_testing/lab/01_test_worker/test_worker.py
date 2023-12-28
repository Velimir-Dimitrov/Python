from unittest import TestCase, main
from worker import Worker


class TestWorker(TestCase):

    def setUp(self):
        self.worker = Worker("Gosho", 200, 100)

    def test_initialization(self):
        self.assertEqual(self.worker.name, "Gosho")
        self.assertEqual(self.worker.salary, 200)
        self.assertEqual(self.worker.energy, 100)

    def test_energy_incremented_after_using_rest_method(self):
        expected_energy = self.worker.energy + 1
        self.worker.rest()
        self.assertEqual(expected_energy, self.worker.energy)

    def test_worker_with_no_energy_tries_to_work(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_money_increased_by_salary_after_work(self):
        expected_money = self.worker.money + self.worker.salary
        self.worker.work()
        self.assertEqual(expected_money, self.worker.money)

    def test_energy_decrease_after_work(self):
        expected_energy = self.worker.energy - 1
        self.worker.work()

        self.assertEqual(expected_energy, self.worker.energy)

    def test_get_info_method(self):
        expected_result = f'{self.worker.name} has saved {self.worker.money} money.'
        current_result = self.worker.get_info()
        self.assertEqual(expected_result, current_result)


if __name__ == "__main__":
    main()