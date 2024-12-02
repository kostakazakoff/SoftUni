from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Simba", "Cat", "Meaow")

    def test__initialising(self):
        self.assertEqual("Simba", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("Meaow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test__make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Simba makes Meaow", result)

    def test__get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)
        self.assertEqual(self.mammal._Mammal__kingdom, result)

    def test__info(self):
        result = self.mammal.info()
        self.assertEqual("Simba is of type Cat", result)


if __name__ == '__main__':
    main()