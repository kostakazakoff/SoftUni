from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    type = "Heavy"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, HeavyHardware.type, capacity * 2, int(memory * 0.75))
