import UDP_server
import UDP_config
from UDP_packet_handler import UDPPacketHandler
from standa import Standa
from custom_positioner import CustomPositioner


class MainApp:
    def __init__(self, udp_config):
        self.udp_server = UDP_server.UDPServer(udp_config.ip_address, udp_config.port)
        self.standa_device = Standa()
        self.custom_positioner_device = CustomPositioner()

        # self.command_parser = command_parser.CommandParser()

    def start(self):
        self.udp_server.start()
        while True:
            packet, address = self.udp_server.receive_packet()
            print(f"packet:{packet}, address:{address}")
            UDPPacketHandler(self.udp_server).handle_packet(packet, address,
                                                            self.standa_device, self.custom_positioner_device)


config = UDP_config.UDPConfig("localhost", 5005)
server = MainApp(config)
server.start()
