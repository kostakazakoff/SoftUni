from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    type = "Power"

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, PowerHardware.type, int(capacity * 0.25), int(memory * 1.75))
