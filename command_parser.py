import struct

class CommandParser:
    def __init__(self):
        self.command_format = "!HH"  # Example format: 2 bytes for command, 2 bytes for parameter

    def parse_command(self, packet):
        command, parameter = struct.unpack(self.command_format, packet)
        return command, parameter