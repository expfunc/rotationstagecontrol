import struct
from standa import Standa


class CommandParser:
    def __init__(self):
        self.standa_device = Standa()
        self.command_list_ids = {'0x0100': self.standa_device.connect,
                                 '0x0101': self.standa_device.disconnect,
                                 '0x0200': self.standa_device.move_absolute,
                                 '0x0201': self.standa_device.move_relative,
                                 '0x0202': self.standa_device.set_speed,
                                 '0x0203': self.standa_device.set_acceleration,
                                 '0x0204': self.standa_device.set_deceleration,
                                 '0x0205': self.standa_device.set_zero,
                                 '0x0206': self.standa_device.abort,
                                 '0x0300': self.standa_device.get_current_position,
                                 # '0x0301': self.standa_device.get_move_settings,
                                 '0x0302': self.standa_device.get_status}

        self.command_format = "!HH"  # Example format: 2 bytes for command, 2 bytes for parameter

    def parse_command(self, packet):
        # command, parameter = struct.unpack(self.command_format, packet)
        # return command, parameter
        command = packet.split()
        if command[0] in ('0x01', '0x02'):
            self.command_list_ids['0x0100'](command[1] if command[1] != '0x01' else r'xi-emu:///C:/virtual_motor/virtual_motor_controller_1.bin')

        match command[0]:
            case '0x01':
                try:
                    self.command_list_ids[command[2]](int(command[3]))
                except ValueError:
                    self.command_list_ids[command[2]]()
            case '0x02':
                self.command_list_ids[command[2]]()
