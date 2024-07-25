from globals import *
from device_manager import DeviceManager


class CommandReceiver:
    def __init__(self):
        self.command = DeviceManager()

    def receive_command(self, packet):
        self.command.execute_command(*packet[2:])

        # if packet[3] == '0x0100':
        #     if packet[2] in devices_dict.keys():
        #         command_dict_ids[packet[3]](devices_dict[packet[2]])
        #     else:
        #         command_dict_ids[packet[3]](packet[2])
        # elif len(packet) == 4:
        #     command_dict_ids[packet[3]]
        # else:
        #     command_dict_ids[packet[3]][0](int(packet[4]))
