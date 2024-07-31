from command_parser import CommandParser
from command_receiver import CommandReceiver
from command_builder import CommandBuilder
from error_bubbling import ErrorBubbling
from UDP_server import UDPServer


class UDPPacketHandler:
    def __init__(self, udp_server):
        self.udp_server = udp_server
        self.error_bubbling = ErrorBubbling()

    def handle_packet(self, packet, address, standa_device, custom_positioner_device):
        # Process the packet and extract commands and parameters
        # For now, just print the packet
        try:
            parsed_command = CommandParser().parse_command(packet)
            if not parsed_command:
                return None
            print(f"Received packet from {address}: {packet}")
            if parsed_command[0] == '0x01':
                CommandReceiver(standa_device, custom_positioner_device).receive_command(parsed_command)
            else:
                UDPServer(address[0], 5005).send_packet(
                    CommandBuilder(self.udp_server, self.error_bubbling.get_error_list(),
                                   standa_device, custom_positioner_device).built_command(parsed_command)
                )
        except Exception as e:
            self.error_bubbling.insert_error(e)
