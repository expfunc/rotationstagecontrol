from device_manager import DeviceManager


class CommandReceiver:
    def __init__(self, standa_device, custom_positioner_device):
        self.command = DeviceManager(standa_device, custom_positioner_device)

    def receive_command(self, packet):
        self.command.execute_command(*packet[2:])
