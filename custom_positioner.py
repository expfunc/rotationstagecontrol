from device import Device
import serial
import serial.tools.list_ports
from time import sleep


class CustomPositioner(Device):
    """
    A class representing a custom positioner device for motion control.

    Attributes:
        serial_port (serial.Serial): The serial port connection to the device.
    """

    def __init__(self):
        """
        Initializes the custom positioner device with no connected serial port.
        """
        self.serial_port = None

    @staticmethod
    def search_for_positioner_devices():
        """
        Searches for connected custom positioner devices.

        Returns:
            list: A list of tuples with information about available serial ports.
        """

        return [tuple(p) for p in list(serial.tools.list_ports.comports())]

    def connect(self, com: str):
        """
        Connects to the custom positioner device using a specified COM port.

        Args:
            com (str): The COM port identifier.
        """
        self.serial_port = serial.Serial(com, 9600, timeout=2)

    def disconnect(self):
        """
        Disconnects the custom positioner device.
        """
        self.serial_port.close()

    def move_absolute(self, *next_position):
        """
        Moves the custom positioner to an absolute position.

        Args:
            next_position (float, °): The target position to move to.
        """
        next_position = next_position[0]
        message = f"move abs {next_position}"
        self.serial_port.write(message.encode())

    def move_relative(self, *next_position):
        """
        Moves the custom positioner relative to its current position.

        Args:
            next_position (float, °): The relative distance to move.
        """
        next_position = next_position[0]
        message = f"move rel {next_position}"
        self.serial_port.write(message.encode())

    def set_speed(self, *speed):
        """
        Sets the movement speed of the custom positioner.

        Args:
            speed (float, °/s): The speed to set.
        """
        speed = speed[0]
        message = f"set speed {speed}"
        self.serial_port.write(message.encode())

    def set_acceleration(self, *acceleration):
        """
        Sets the acceleration of the custom positioner.

        Args:
            acceleration (float, °/s²): The acceleration to set.
        """
        acceleration = acceleration[0]
        message = f"set acc {acceleration}"
        self.serial_port.write(message.encode())
        self.serial_port.flush()

    def set_deceleration(self, *deceleration):
        """
        Sets the deceleration of the custom positioner.

        Args:
            deceleration (float, °/s²): The deceleration to set.
        """
        deceleration = deceleration[0]
        message = f"set dec {deceleration}"
        self.serial_port.write(message.encode())

    def set_zero(self):
        """
        Sets the current position of the custom positioner as zero.
        """
        message = f"set zero"
        self.serial_port.write(message.encode())

    def abort(self):
        """
        Aborts any ongoing movement of the custom positioner.
        """
        message = f"abort"
        self.serial_port.write(message.encode())

    def get_position(self):
        """
        Gets the current position of the custom positioner.

        Returns:
            str, °: The current position.
        """
        self.serial_port.reset_output_buffer()
        message = f"get angle"
        self.serial_port.write(message.encode())
        position = self.serial_port.readline().split()[-1].decode()
        return position

    def get_move_settings(self):
        """
        Gets the current movement settings (speed, acceleration, deceleration).

        Returns:
            tuple: The current speed, acceleration, and deceleration settings (°/s, °/s², °/s²).
        """
        self.serial_port.reset_output_buffer()
        messages = (f"get speed", f"get acc", f"get dec")
        for message in messages:
            self.serial_port.write(message.encode())
        move_settings = tuple(map(lambda x: float(x.decode().strip().split()[-1]), self.serial_port.readlines()[-3:]))
        return move_settings

    def get_status(self):
        """
        Gets the current status of the custom positioner.

        Returns:
            str: The status of the device.
        """
        self.serial_port.reset_output_buffer()
        message = f"status"
        self.serial_port.write(message.encode())
        return ''.join(map(bytes.decode, self.serial_port.readlines()))

    def info(self):
        """
        Retrieves information about the custom positioner device.

        Returns:
            str: The device information.
        """
        self.serial_port.reset_output_buffer()
        message = f"info\r\n"
        self.serial_port.write(message.encode())
        return ''.join(map(bytes.decode, self.serial_port.readlines()[-2:]))

    def DropMessage(self):
        """
        Drops single message.
        """
        message = f"test\r\n"
        self.serial_port.write(message.encode())
        print(self.serial_port.readlines())
