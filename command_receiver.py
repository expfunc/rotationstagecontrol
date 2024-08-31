from device_manager import DeviceManager


class CommandReceiver:
    """
    A class that processes and executes commands received from a device.

    Attributes:
        command (DeviceManager): An instance of DeviceManager to execute the commands.
    """

    def __init__(self, standa_device, custom_positioner_device, device_map):
        """
        Initializes the CommandReceiver with devices and a device map.

        Args:
            standa_device (Standa): The Standa device instance.
            custom_positioner_device (CustomPositioner): The custom positioner device instance.
            device_map (dict): A map of device IDs to device instances.
        """
        self.command = DeviceManager(standa_device, custom_positioner_device, device_map)

    def receive_command(self, packet):
        """
        Receives and processes a command packet.

        Args:
            packet (list): The packet containing the command.

        Raises:
            ValueError: If the packet type or command is invalid.
        """
        packet_type = packet[0]
        if packet[3].startswith('0x02') or packet[3].startswith('0x01'):
            self.command.execute_command(*packet[2:])
        else:
            raise ValueError(f"Packet type {packet_type} doesn't have command {packet[3]}")
