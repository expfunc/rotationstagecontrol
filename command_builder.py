from globals import *


def convert(data: str):
    return bytes(map(ord, data))


class CommandBuilder:
    def __init__(self, udp_server, error_list):
        self.udp_server = udp_server
        self.error_list = error_list

    def command_built(self, packet):
        packet_type = packet[0]
        match packet_type:
            case '0x02':
                self.udp_server.send_packet(convert(command_dict_ids[packet[3]]()))
            case '0x03':
                self.udp_server.send_packet(convert(f'{self.error_list}'))
            case '0x08':
                self.udp_server.send_packet(convert(f'Standa devices: {standa_device.search_for_standa_devices()}'
                                            f'\nPositioner devices: {positioner_device.search_for_positioner_devices()}'))
