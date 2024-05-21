import UDP_server
import command_parser

class MainApp:
    def __init__(self, udp_config):
        self.udp_server = UDP_server.UDPServer(udp_config.ip_address, udp_config.port)
        self.command_parser = command_parser.CommandParser()

    def start(self):
        self.udp_server.start()
        while True:
            packet, address = self.udp_server.receive_packet()
            command, parameter = self.command_parser.parse_command(packet)
