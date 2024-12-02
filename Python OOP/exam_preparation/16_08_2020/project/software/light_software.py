from project.software.software import Software


class LightSoftware(Software):
    type = "Light"

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, LightSoftware.type, int(capacity_consumption * 1.5), int(memory_consumption * 0.5))
