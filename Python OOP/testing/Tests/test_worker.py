from unittest import TestCase, main
from Worker.worker import Worker


class WorkerTests(TestCase):
    def setUp(self):
        self.worker = Worker("Kosta", 2000, 100)

    def test_correct_initialising(self):
        self.assertEqual("Kosta", self.worker.name)
        self.assertEqual(2000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_worker_energy_increments_when_rest(self):
        self.worker.energy = 99
        self.worker.rest()
        self.assertEqual(100, self.worker.energy)

    def test_worker_works_with_less_than_1_energy(self):
        self.worker.energy = 0
        with self.assertRaises(Exception) as ex:
            self.worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_increase_salary_when_worker_work(self):
        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)

    def test_worker_energy_decreasing_when_work(self):
        self.worker.work()
        self.assertEqual(99, self.worker.energy)

    def test_worker_get_info_method(self):
        self.assertEqual('Kosta has saved 0 money.', self.worker.get_info())


if __name__ == '__main__':
    main()
