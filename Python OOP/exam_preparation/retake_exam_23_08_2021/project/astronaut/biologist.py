from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    BREATHE_VALUE = 5

    def __init__(self, name):
        super().__init__(name, 70)
