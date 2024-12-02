from abc import ABC, abstractmethod


class Car(ABC):

    def __init__(self, model: str, speed_limit: int):
        self.model = model
        self.speed_limit = speed_limit
        self.is_taken: bool = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if len(value) < 4:
            raise ValueError(f"Model {value} is less than 4 symbols!")
        self.__model = value

    @property
    def speed_limit(self):
        return self.__speed_limit

    @speed_limit.setter
    def speed_limit(self, value):
        if value not in range(self.min_speed_limit, self.max_speed_limit + 1):
            raise ValueError(f"Invalid speed limit! Must be between "
                             f"{self.min_speed_limit} and "
                             f"{self.max_speed_limit}!")
        self.__speed_limit = value

    @property
    @abstractmethod
    def min_speed_limit(self) -> int:
        return 0

    @property
    @abstractmethod
    def max_speed_limit(self) -> int:
        return 0
