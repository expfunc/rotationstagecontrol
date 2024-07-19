import UDP_server
from command_parser import CommandParser
import UDP_config

class MainApp:
    def __init__(self, udp_config):
        self.udp_server = UDP_server.UDPServer(udp_config.ip_address, udp_config.port)
        # self.command_parser = command_parser.CommandParser()

    def start(self):
        self.udp_server.start()
        while True:
            packet, address = self.udp_server.receive_packet()
            print(f"packet:{packet}, address:{address}")
            # command, parameter = CommandParser().parse_command(packet)
            # print(command, parameter)
            command = CommandParser().parse_command(packet)
            # print(command)

config = UDP_config.UDPConfig("localhost", 5005)
server = MainApp(config)
server.start()
