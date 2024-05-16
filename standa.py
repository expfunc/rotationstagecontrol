from device import Device
import libximc.highlevel as ximc

class Standa(Device):
    def __init__(self):
        super().__init__("Standa")
        self.axis = None
        self.add_command("search_for_devices", self.search_for_devices)
        self.add_command("connect", self.connect)
        self.add_command("disconnect", self.disconnect)
        self.add_command("move_absolute", self.move_absolute)
        self.add_command("move_relative", self.move_relative)
        self.add_command("set_acceleration", self.set_acceleration)
        self.add_command("set_deacceleration", self.set_deacceleration)
        self.add_command("set_speed", self.set_speed)
        self.add_command("get_current_position", self.get_current_position)
        self.add_command("set_zero", self.set_zero)

    # Search for active devices
    def search_for_devices(self):
        devices = ximc.enumerate_devices(
            ximc.EnumerateFlags.ENUMERATE_NETWORK |
            ximc.EnumerateFlags.ENUMERATE_PROBE
        )

        if len(devices) == 0:
            print("The real devices were not found. A virtual device will be used.")
        else:
            # Print real devices list
            print("Found {} real device(s):".format(len(devices)))
            for device in devices:
                print("  {}".format(device))

    # Connection and disconnection
    def connect(self, device_uri):
        self.axis = ximc.Axis(device_uri)
        self.axis.open_device()

    def disconnect(self):
        self.axis.close_device()

    # Motion commands
    def move_absolute(self, next_position):
        self.axis.command_move(next_position, 0)

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
    def get_current_position(self):
        position = self.axis.get_position()

        return print("Current position:", position.Position)

    # Set current position as zero
    def set_zero(self):
        self.axis.command_zero()
