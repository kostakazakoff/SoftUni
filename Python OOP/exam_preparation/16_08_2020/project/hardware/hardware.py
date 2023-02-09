from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.memory = memory
        self.software_components = []

    def install(self, software: Software):
        if software.memory_consumption > self.memory or software.capacity_consumption > self.capacity:
            raise Exception("Software cannot be installed")
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.software_components.remove(software)

    def __repr__(self):
        return f"Hardware Component - {self.name}\n" \
               f"Express Software Components: " \
               f"{len([x for x in self.software_components if x.software_type == 'Express'])}\n" \
               f"Light Software Components: " \
               f"{len([x for x in self.software_components if x.software_type == 'Light'])}\n"\
               f"Memory Usage: {sum([x.memory_consumption for x in self.software_components])} / {self.memory}\n" \
               f"Capacity Usage: " \
               f"{sum([x.capacity_consumption for x in self.software_components])} / " \
               f"{self.capacity}\n" \
               f"Type: {self.hardware_type}\n" \
               f"Software Components: {', '.join(x.name for x in self.software_components) if self.software_components else 'None'}"
