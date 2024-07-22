import struct
from standa import Standa
from utils import Utils


class CommandParser:
    def __init__(self):
        self.standa_device = Standa()
        self.command_dict_ids = {b'0x0100': self.standa_device.connect,
                                 b'0x0101': self.standa_device.disconnect,
                                 b'0x0200': (self.standa_device.move_absolute, float),
                                 b'0x0201': (self.standa_device.move_relative, float),
                                 b'0x0202': (self.standa_device.set_speed, float),
                                 b'0x0203': (self.standa_device.set_acceleration, float),
                                 b'0x0204': (self.standa_device.set_deceleration, float),
                                 b'0x0205': self.standa_device.set_zero,
                                 b'0x0206': self.standa_device.abort,
                                 b'0x0300': self.standa_device.get_current_position,
                                 # b'0x0301': self.standa_device.get_move_settings,
                                 b'0x0302': self.standa_device.get_status}
        self.devices_dict = {0x01: r'xi-emu:///C:/virtual_motor/virtual_motor_controller_1.bin'}

        self.command_format = "!HH"  # Example format: 2 bytes for command, 2 bytes for parameter

    def parse_command(self, packet):
        packet = tuple(packet.split())
        bytearray_crc = bytearray(b' '.join(packet[:-1]))
        crc_calc = Utils.generate_CRC16(bytearray(b' '.join(packet[:-1])), 0, len(bytearray_crc))
        crc = int(packet[-1], 16)
        if crc != int(crc_calc.hex(), 16):
            raise TypeError("CRC Mismatch")
        packet_type = hex(int(packet[0], 16))
        if packet_type in (0x01, 0x02):
            if type(self.command_dict_ids[packet[3]]) is tuple:
                return packet[:4] + [self.command_dict_ids[packet[3]][1](packet[4])]
        return packet[:-1]
