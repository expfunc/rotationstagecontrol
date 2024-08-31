from device_manager import DeviceManager


def convert(data: str):
    """
    Converts a string to its UTF-8 encoded byte representation.

    Args:
        data (str): The string to convert.

    Returns:
        bytes: UTF-8 encoded bytes of the string.
    """
    return data.encode('utf-8')


class CommandBuilder:
    """
    A class to build and execute commands based on received packets.

    Attributes:
        udp_server (UDPServer): The UDP server instance.
        error (str): An optional error message.
        command (DeviceManager): An instance of DeviceManager to execute the commands.
    """

    def __init__(self, udp_server, standa_device, custom_positioner_device, device_map, error=None):
        """
        Initializes the CommandBuilder with server, devices, and an optional error.

        Args:
            udp_server (UDPServer): The UDP server instance.
            standa_device (Standa): The Standa device instance.
            custom_positioner_device (CustomPositioner): The custom positioner device instance.
            device_map (dict): A map of device IDs to device instances.
            error (str, optional): An error message, if any. Defaults to None.
        """
        self.udp_server = udp_server
        self.error = error
        self.command = DeviceManager(standa_device, custom_positioner_device, device_map)

    def built_command(self, packet):
        """
        Builds and executes the command based on the packet type.

        Args:
            packet (list): The packet containing the command.

        Returns:
            bytes: The result of the command execution.

        Raises:
            ValueError: If the packet type or command is invalid.
        """
        packet_type = packet[0]
        match packet_type:
            case '0x02':
                if packet[3].startswith('0x03'):
                    return convert(f'{self.command.execute_command(*packet[2:])}\n')
                else:
                    raise ValueError(f"Packet type {packet_type} doesn't have command {packet[3]}")
            case '0x03':
                return convert(f'{self.error}\n')
            case '0x08':
                return convert("Standa devices: {}, Custom Positioner devices: {}\n".format(*self.command.search_devices()))
            case _:
                raise ValueError(f"Unknown packet type: {packet_type}")
