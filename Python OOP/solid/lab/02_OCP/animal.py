from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def __init__(self, species):
        self.species = species

    @abstractmethod
    def animal_sound(self):
        ...


class Cat(Animal):
    def __init__(self, species):
        super().__init__(species)
        self.species = species

    def animal_sound(self):
        print('meow')


class Dog(Animal):
    def __init__(self, species):
        super().__init__(species)
        self.species = species

    def animal_sound(self):
        print('woof-woof')


class Chicken(Animal):
    def __init__(self, species):
        super().__init__(species)
        self.species = species

    def animal_sound(self):
        print('piu-piu')


def animal_sound(animals: list):
    for animal in animals:
        animal.animal_sound()


animals = [Cat('cat'), Dog('dog'), Chicken('chicken')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
