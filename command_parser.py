from utils import Utils

class CommandParser:
    def __init__(self):
        self.command_format = "!HH"  # Example format: 2 bytes for command, 2 bytes for parameter

    def parse_command(self, packet):
        packet = tuple(packet.split())
        bytearray_crc = bytearray(map(ord, ' '.join(packet[:-1])))
        crc_calc = Utils.generate_CRC16(bytearray_crc, 0, len(bytearray_crc))
        crc = int(packet[-1], 16)
        if crc != int(crc_calc.hex(), 16):
            raise TypeError("CRC Mismatch")
        # packet_type = hex(int(packet[0], 16))
        # if packet_type in ('0x01', '0x02'):
        #     if type(command_dict_ids[packet[3]]) is tuple:
        #         return packet[:4] + [command_dict_ids[packet[3]][1](packet[4])]
        return packet[:-1]
