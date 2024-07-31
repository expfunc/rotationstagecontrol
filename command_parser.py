from utils import Utils

class CommandParser:
    def __init__(self):
        self.command_format = "!HH"  # Example format: 2 bytes for command, 2 bytes for parameter

    def parse_command(self, packet: str):
        if any((packet.startswith('[Device Response]'), packet.startswith('[Error]'), packet.startswith('[Devices]'))):
            return None
        packet = tuple(packet.split())
        bytearray_crc = bytearray(' '.join(packet[:-1]).encode('utf-8'))
        crc_calc = int(Utils.generate_CRC16(bytearray_crc, 0, len(bytearray_crc)).hex(), 16)
        crc = int(packet[-1], 16)
        if crc != crc_calc:
            raise ValueError("CRC Mismatch")
        return packet[:-1]
