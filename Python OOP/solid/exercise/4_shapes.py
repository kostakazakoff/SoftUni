from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        ...


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height / 2


class AreaCalculator:
    def __init__(self, list_of_shapes):
        self.shapes = list_of_shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        assert isinstance(value, list), "`shapes` should be of type `list`."
        self.__shapes = value

    @property
    def total_area(self):
        all_areas = []
        [all_areas.append(shape.calculate_area()) for shape in self.shapes]
        return sum(all_areas)


# Test ------------------------------------------------------------------------
# shapes = [Rectangle(1, 6), Triangle(2, 3)]
# calculator = AreaCalculator(shapes)
# print("The total area is: ", calculator.total_area)
