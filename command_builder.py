# from globals import *
from device_manager import DeviceManager


def convert(data: str):
    return bytes(map(ord, data))


class CommandBuilder:
    def __init__(self, udp_server, error_list, standa_device, custom_positioner_device):
        self.udp_server = udp_server
        self.error_list = error_list
        self.command = DeviceManager(standa_device, custom_positioner_device)

    def built_command(self, packet):
        packet_type = packet[0]
        match packet_type:
            case '0x02':
                self.udp_server.send_packet(convert(self.command.execute_command(*packet[2:])))
            case '0x03':
                self.udp_server.send_packet(convert(f'{self.error_list}'))
            case '0x08':
                pass
                # self.udp_server.send_packet(convert(f'Standa devices: {standa_device.search_for_standa_devices()}'
                # f'\nPositioner devices: {positioner_device.search_for_positioner_devices()}'))
