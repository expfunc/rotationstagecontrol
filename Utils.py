class Utils:
    """
    A collection of utility methods for various tasks.

    Methods:
        crc16(data): Generates a CRC-16 checksum for the given bytearray data.
    """

    @staticmethod
    def generate_CRC16(data: bytearray, offset: int, length: int) -> bytes:
        """
        Generates a CRC-16 (Cyclic Redundancy Check) checksum for a specified range of bytes within the given bytearray data.

        Args:
            data (bytearray): The input data for which to generate the CRC-16 checksum.
            offset (int): The starting offset within the data bytearray from which to begin calculating the CRC-16 checksum.
            length (int): The number of bytes from the offset to include in the CRC-16 checksum calculation.

        Returns:
            bytes: The 2-byte CRC-16 checksum.

        Notes:
            This implementation uses the CRC-16/CCITT-FALSE polynomial (0x1021) to calculate the checksum.
            The initial CRC value is set to 0xFFFF, which is the standard initial value for CRC-16.
        """
        if data is None or offset < 0 or offset > len(data) - 1 and offset + length > len(data):
            return b'\x00'
        crc = 0xFFFF
        for i in range(0, length):
            crc ^= data[offset + i] << 8
            for j in range(0, 8):
                if (crc & 0x8000) > 0:
                    crc = (crc << 1) ^ 0x1021
                else:
                    crc = crc << 1
        return (crc & 0xFFFF).to_bytes(2, 'big')
