import unittest
from Utils import Utils


class TestUtils(unittest.TestCase):
    def test_crc16_empty_input(self):
        data = bytearray()
        self.assertEqual(b'\xFF\xFF', Utils.generate_CRC16(data, 0, len(data)))

    def test_crc16_single_byte(self):
        data = bytearray(b'\x01')
        self.assertEqual(b'\xF1\xD1', Utils.generate_CRC16(data, 0, len(data)))

    def test_crc16_short_string(self):
        data = bytearray(b'Hello')
        self.assertEqual(b'\xDA\xDA', Utils.generate_CRC16(data, 0, len(data)))

    def test_crc16_long_string(self):
        data = bytearray(b'Hello, World')
        self.assertEqual(b'\xB2\xD4', Utils.generate_CRC16(data, 0, len(data)))

if __name__ == '__main__':
    unittest.main()
