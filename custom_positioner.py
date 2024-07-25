from device import Device
import serial
import serial.tools.list_ports

class CustomPositioner(Device):
    def __init__(self):
        self.serial_port = None

    def search_for_positioner_devices(self):
        return [tuple(p) for p in list(serial.tools.list_ports.comports())]

    # Connection and disconnection
    def connect(self):
        self.serial_port = serial.Serial('COM3', 9600, timeout=1)

    def disconnect(self):
        self.serial_port.close()

    def move_absolute(self, next_position):
        print(next_position)
        message = f"move abs {next_position}"
        self.serial_port.write(message.encode())

    # Motion commands
    def move_relative(self, next_position):
        message = f"move rel {next_position}"
        self.serial_port.write(message.encode())

    def set_speed(self, speed):
        message = f"set speed {speed}"
        self.serial_port.write(message.encode())

    def set_acceleration(self, acceleration):
        message = f"set acc {acceleration}"
        self.serial_port.write(message.encode())

    def set_deceleration(self, deceleration):
        message = f"set acc {deceleration}"
        self.serial_port.write(message.encode())

    def set_zero(self):
        message = f"set zero"
        self.serial_port.write(message.encode())

    def abort(self):
        message = f"abort"
        self.serial_port.write(message.encode())

    def get_position(self):
        message = f"get angle"
        self.serial_port.write(message.encode())
        self.serial_port.flush()
        return self.serial_port.readline().split()[-1].decode()

    def get_move_settings(self):
        messages = (f"get speed", f"get acc", f"get dec")
        for message in messages:
            self.serial_port.write(message.encode())
            self.serial_port.flush()
        return tuple(map(lambda x: x.decode().strip(), self.serial_port.readlines()))

    def get_status(self):
        # message = f"status"
        # self.serial_port.write(message.encode())
        pass

    def info(self):
        message = f"info"
        self.serial_port.write(message.encode())
        self.serial_port.flush()
        return ''.join(map(bytes.decode, self.serial_port.readlines()))
