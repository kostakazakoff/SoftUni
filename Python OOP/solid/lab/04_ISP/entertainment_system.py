class EntertainmentDevice:
    def connect_device_to_power_outlet(self): pass


class HDMIInterface:
    def connect_to_device_via_hdmi_cable(self): pass


class RCAInterface:
    def connect_to_device_via_rca_cable(self): pass


class EthernetInterface:
    def connect_to_device_via_ethernet_cable(self): pass


class Television(EntertainmentDevice, HDMIInterface, RCAInterface):
    def connect_to_dvd(self, dvd_player):
        self.connect_to_device_via_rca_cable(dvd_player)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_hdmi_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class DVDPlayer(EntertainmentDevice, HDMIInterface):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class GameConsole(EntertainmentDevice, HDMIInterface, EthernetInterface):
    def connect_to_tv(self, television):
        self.connect_to_device_via_hdmi_cable(television)

    def connect_to_router(self, router):
        self.connect_to_device_via_ethernet_cable(router)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)


class Router(EntertainmentDevice, EthernetInterface):
    def connect_to_tv(self, television):
        self.connect_to_device_via_ethernet_cable(television)

    def connect_to_game_console(self, game_console):
        self.connect_to_device_via_ethernet_cable(game_console)

    def plug_in_power(self):
        self.connect_device_to_power_outlet(self)
