from device import Device
import serial

class Positioner(Device):
    def __init__(self):
        super().__init__("Positioner")
        self.serial_port = None
        self.add_command("search_for_devices", self.search_for_devices)

    # Connection and disconnection
    def connect(self, device_uri):
        self.serial_port = serial.Serial('COM3', 9600, timeout=1)
        self.serial_port.open()

    def disconnect(self):
        self.serial_port.close()

    # Motion commands
    def move_relative(self, next_position):
        message = f"pwm angle {next_position}"
        self.serial_port.write(message.encode())

    # def change_rotation_direction(self, go_forward: bool):
    #     if go_forward:
    #         message = f"pwm dir"
    #         self.serial_port.write(message.encode())
    #     else:
    #         message = f"pwm dir"
    #         self.serial_port.write(message.encode())

