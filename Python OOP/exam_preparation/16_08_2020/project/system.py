from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:

    _hardware = []
    _software = []

    @staticmethod
    def _find_hardware_by_name(hardware_name: str):
        hardware = [x for x in System._hardware if x.name == hardware_name]
        if hardware:
            return hardware[0]

    @staticmethod
    def _find_software_by_name(software_name: str):
        software = [x for x in System._software if x.name == software_name]
        if software:
            return software[0]

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System._find_hardware_by_name(hardware_name)
        if not hardware:
            return "Hardware does not exist"
        software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        hardware = System._find_hardware_by_name(hardware_name)
        if not hardware:
            return "Hardware does not exist"
        software = LightSoftware(name, capacity_consumption, memory_consumption)
        hardware.install(software)
        System._software.append(software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        hardware = System._find_hardware_by_name(hardware_name)
        software = System._find_software_by_name(software_name)
        if not all([hardware, software]):
            return "Some of the components do not exist"
        hardware.uninstall(software)
        System._software.remove(software)

    @staticmethod
    def analyze():
        return f"System Analysis\n" \
             f"Hardware Components: {len(System._hardware)}\n" \
             f"Software Components: {len(System._software)}\n" \
             f"Total Operational Memory: " \
             f"{sum(x.memory_consumption for x in System._software)} / " \
             f"{sum(x.memory for x in System._hardware)}\n" \
             f"Total Capacity Taken: " \
             f"{sum(x.capacity_consumption for x in System._software)} / " \
             f"{sum(x.capacity for x in System._hardware)}"

    @staticmethod
    def system_split():
        output = []
        for component in System._hardware:
            output.append(component.__repr__())
        return '\n'.join(output)
