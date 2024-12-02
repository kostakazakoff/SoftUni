from unittest import TestCase, main
from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(2)

    def test__initialising(self):
        self.assertEqual(2, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test__size_setter(self):
        with self.assertRaises(ValueError) as error:
            self.plantation.size = -1
        self.assertEqual("Size must be positive number!", str(error.exception))

    def test__hire_worker(self):
        result = self.plantation.hire_worker('Worker')
        self.assertEqual(['Worker'], self.plantation.workers)
        self.assertEqual('Worker successfully hired.', result)

        with self.assertRaises(ValueError) as error:
            self.plantation.hire_worker('Worker')
        self.assertEqual("Worker already hired!", str(error.exception))

    def test__len__(self):
        self.assertEqual(0, self.plantation.__len__())
        self.plantation.plants = {'Worker': ['a', 'b'], 'Worker1': ['a']}
        self.assertEqual(3, self.plantation.__len__())

    def test__planting(self):
        self.plantation.hire_worker('Worker')
        result = self.plantation.planting('Worker', 'plant')
        self.assertEqual(['plant'], self.plantation.plants['Worker'])
        self.assertEqual({'Worker': ['plant']}, self.plantation.plants)
        self.assertEqual("Worker planted it's first plant.", result)

        result = self.plantation.planting('Worker', 'plant2')
        self.assertEqual(['plant', 'plant2'], self.plantation.plants['Worker'])
        self.assertEqual({'Worker': ['plant', 'plant2']}, self.plantation.plants)
        self.assertEqual("Worker planted plant2.", result)

        with self.assertRaises(ValueError) as error:
            self.plantation.planting('NoWorker', 'plant')
        self.assertEqual("Worker with name NoWorker is not hired!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.plantation.planting('Worker', 'plant')
        self.assertEqual("The plantation is full!", str(error.exception))

    def test__str__(self):
        self.plantation.size = 3
        self.plantation.hire_worker('Worker')
        self.plantation.hire_worker('Worker1')
        self.plantation.plants = {'Worker': ['a', 'b'], 'Worker1': ['b']}
        expected = "Plantation size: 3\n" \
                   "Worker, Worker1\n" \
                   "Worker planted: a, b\n" \
                   "Worker1 planted: b"
        self.assertEqual(expected, self.plantation.__str__())

    def test__repr__(self):
        self.plantation.size = 3
        self.plantation.hire_worker('Worker')
        self.plantation.hire_worker('Worker1')
        expected = 'Size: 3\nWorkers: Worker, Worker1'
        self.assertEqual(expected, self.plantation.__repr__())

    if __name__ == '__main__':
        main()
