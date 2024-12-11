from utils import Utils


class CommandParser:
    """A class responsible for parsing and validating commands received in packets"""

    def __init__(self):
        """
        Initializes the CommandParser with a specific command format.
        """
        self.command_format = "!HH"  # Example format: 2 bytes for command, 2 bytes for parameter

    def parse_command(self, packet: str):
        """
        Parses a packet string and validates its CRC.

        Args:
            packet (str): The packet to be parsed.

        Returns:
            tuple: Parsed packet data excluding the CRC.

        Raises:
            ValueError: If the CRC does not match the calculated value.
        """
        packet = tuple(packet.split())
        bytearray_crc = bytearray(' '.join(packet[:-1]).encode('utf-8'))
        crc_calc = int(Utils.generate_CRC16(bytearray_crc, 0, len(bytearray_crc)).hex(), 16)
        crc = int(packet[-1], 16)
        if crc != crc_calc:
            raise ValueError("CRC Mismatch")
        return packet[:-1]
