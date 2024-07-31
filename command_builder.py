from device_manager import DeviceManager


def convert(data: str):
    return data.encode('utf-8')


class CommandBuilder:
    def __init__(self, udp_server, error_list, standa_device, custom_positioner_device):
        self.udp_server = udp_server
        self.error_list = error_list
        self.command = DeviceManager(standa_device, custom_positioner_device)

    def built_command(self, packet):
        packet_type = packet[0]
        match packet_type:
            case '0x02':
                return convert(f'[Device Response] {self.command.execute_command(*packet[2:])}')
            case '0x03':
                return convert(f'[Error] {self.error_list}')
            case '0x08':
                return convert("[Devices]\nStanda devices: {}, Custom Positioner devices: {}".format(*self.command.search_devices()))
            case _:
                raise ValueError(f"Unknown packet type: {packet_type}")
