from device import Device
import libximc.highlevel as ximc


class Standa(Device):
    def __init__(self):
        self.axis = None

    # Search for active devices
    @staticmethod
    def search_for_standa_devices():
        devices = ximc.enumerate_devices(
            ximc.EnumerateFlags.ENUMERATE_NETWORK |
            ximc.EnumerateFlags.ENUMERATE_PROBE
        )

        return devices

    # Connection and disconnection
    def connect(self, device_uri):
        self.axis = ximc.Axis(device_uri)
        self.axis.open_device()

    def disconnect(self):
        self.axis.close_device()

    # Motion commands
    def move_absolute(self, next_position: int):
        self.axis.command_move(int(next_position), 0)

    def move_relative(self, relative_shift):
        self.axis.command_movr(relative_shift, 0)

    # Move settings
    def set_acceleration(self, acceleration):
        move_settings = self.axis.get_move_settings()
        move_settings.Accel *= acceleration

    def set_deceleration(self, deceleration):
        move_settings = self.axis.get_move_settings()
        move_settings.Decel *= deceleration

    def set_speed(self, speed):
        move_settings = self.axis.get_move_settings()
        move_settings.Speed *= speed

    # Get current position
    def get_position(self):
        position = self.axis.get_position()
        return f'"Current position:", {position.Position}'

    def get_status(self):
        status = self.axis.get_status()
        return f'"Current move settings:", {status}'

    # Set current position as zero
    def info(self):
        info = self.axis.get_device_information()
        return f'"Device information": {info}'

    def set_zero(self):
        self.axis.command_zero()

    def abort(self):
        self.axis.command_sstp()

