from command_parser import CommandParser
from command_receiver import CommandReceiver
from command_builder import CommandBuilder
from UDP_server import UDPServer

class UDPPacketHandler:
    """
    A class to handle UDP packets by parsing, processing, and responding to them.

    Attributes:
        udp_server (UDPServer): The UDP server instance used for communication.
    """

    def __init__(self, udp_server):
        """
        Initializes the UDPPacketHandler with a UDP server instance.

        Args:
            udp_server (UDPServer): The UDP server instance.
        """
        self.udp_server = udp_server

    def handle_packet(self, packet, address, standa_device, custom_positioner_device, device_map):
        """
        Handles an incoming packet by parsing it and executing the appropriate command.

        Args:
            packet (str): The packet received from the client.
            address (tuple): The address of the client.
            standa_device (Standa): The Standa device instance.
            custom_positioner_device (CustomPositioner): The custom positioner device instance.
            device_map (dict): A map of device IDs to device instances.

        Raises:
            Exception: If an error occurs during command processing.
        """
        try:
            parsed_command = CommandParser().parse_command(packet)
            print(f"Received packet from {address}: {packet}")
            if parsed_command[0] == '0x01':
                CommandReceiver(standa_device, custom_positioner_device, device_map).receive_command(parsed_command)
            else: 
                UDPServer(address[0], 5005).send_packet(
                    CommandBuilder(self.udp_server,
                                   standa_device, custom_positioner_device, device_map).built_command(parsed_command)
                                   )
        except Exception as e:
            UDPServer(address[0], 5005).send_packet(
                    CommandBuilder(self.udp_server,
                                   standa_device, custom_positioner_device, device_map, error=str(e)).built_command(['0x03'])
                                   )
