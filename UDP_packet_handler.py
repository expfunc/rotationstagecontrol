from command_parser import CommandParser
from command_receiver import CommandReceiver
from command_builder import CommandBuilder
from error_bubbling import ErrorBubbling


class UDPPacketHandler:
    def __init__(self, udp_server):
        self.udp_server = udp_server
        self.errorbubbling = ErrorBubbling()

    def handle_packet(self, packet, address, standa_device, custom_positioner_device):
        # Process the packet and extract commands and parameters
        # For now, just print the packet
        print(f"Received packet from {address}: {packet}")
        # try:
        parsed_command = CommandParser().parse_command(packet)
        if parsed_command[0] == '0x01':
            CommandReceiver(standa_device, custom_positioner_device).receive_command(parsed_command)
        else:
            CommandBuilder(self.udp_server, self.errorbubbling.get_error_list(), standa_device, custom_positioner_device).built_command(parsed_command)
        # except Exception as e:
        #     self.errorbubbling.insert_error(e)
