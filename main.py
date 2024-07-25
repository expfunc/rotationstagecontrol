import UDP_server
from command_parser import CommandParser
from command_builder import CommandBuilder
from command_receiver import CommandReceiver
import UDP_config
from error_bubbling import ErrorBubbling
from UDP_packet_handler import UDPPacketHandler


class MainApp:
    def __init__(self, udp_config):
        self.udp_server = UDP_server.UDPServer(udp_config.ip_address, udp_config.port)

        # self.command_parser = command_parser.CommandParser()

    def start(self):
        self.udp_server.start()
        while True:
            packet, address = self.udp_server.receive_packet()
            print(f"packet:{packet}, address:{address}")
            if not UDPPacketHandler(self.udp_server).handle_packet(packet, address):
                continue


config = UDP_config.UDPConfig("localhost", 5005)
server = MainApp(config)
server.start()
