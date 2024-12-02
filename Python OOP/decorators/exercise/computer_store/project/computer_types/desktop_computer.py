from project.computer_types.computer import Computer
from math import log2


class DesktopComputer(Computer):
    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    @property
    def processors(self):
        return {'AMD Ryzen 7 5700G': 500, 'Intel Core i5-12600K': 600, 'Apple M1 Max': 1800}

    @property
    def max_ram(self):
        return 128

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.processors:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        
        if not self.ram_is_valid(ram) or ram > self.max_ram:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
        
        self.processor = processor
        self.ram = ram
        self.price = int(log2(ram)) * 100 + self.processors[processor]
        return f"Created {self.manufacturer} {self.model} with " \
               f"{self.processor} and {self.ram}GB RAM for {self.price}$."

    

