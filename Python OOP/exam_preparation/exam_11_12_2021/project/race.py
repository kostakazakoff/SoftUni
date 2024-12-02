class Race:
    def __init__(self, name: str):
        self.name = name
        self.drivers: object = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) == 0:
            raise ValueError("Name cannot be an empty string!")
        self.__name = value
