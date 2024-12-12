from device import Device
import libximc.highlevel as ximc


class Standa(Device):
    """
    A class representing a Standa device for motion control.

    Attributes:
        axis (ximc.Axis): The axis of the Standa device.
    """

    def __init__(self):
        """
        Initializes the Standa device with no connected axis.
        """
        self.axis = None

    @staticmethod
    def search_for_standa_devices():
        """
        Searches for active Standa devices.

        Returns:
            list: A list of device URIs found on the network and connected ports.
        """
        devices = ximc.enumerate_devices(
            ximc.EnumerateFlags.ENUMERATE_NETWORK |
            ximc.EnumerateFlags.ENUMERATE_PROBE |
            ximc.EnumerateFlags.ENUMERATE_ALL_COM
        )
        return list(map(lambda dev: dev['uri'], devices))

    def connect(self, device_uri):
        """
        Connects to a Standa device using its URI.

        Args:
            device_uri (str): The URI of the device to connect to.
        """
        self.axis = ximc.Axis(device_uri)
        self.axis.open_device()
        step_to_deg_conversion_coeff = 3 / 200
        self.engine_settings = self.axis.get_engine_settings()
        self.axis.set_calb(step_to_deg_conversion_coeff, self.engine_settings.MicrostepMode)

    def disconnect(self):
        """
        Disconnects the Standa device.
        """
        self.axis.close_device()

    def move_absolute(self, *next_position):
        """
        Moves the Standa device to an absolute position.

        Args:
            next_position (float, °): The target position to move to.
        """
        next_position = next_position[0]
        self.axis.command_move_calb(int(next_position))

    def move_relative(self, *relative_shift):
        """
        Moves the Standa device relative to its current position.

        Args:
            relative_shift (float, °): The relative distance to move.
        """
        relative_shift = relative_shift[0]
        self.axis.command_movr_calb(int(relative_shift))

    def move_absolute_unwrapped(self, *next_position):
        raise NotImplementedError("This command is not currently implemented.")

    def set_speed(self, *speed):
        """
        Sets the movement speed of the Standa device.

        Args:
            speed (float, °/s): The speed to set.
        """
        speed = speed[0]
        move_settings = self.axis.get_move_settings_calb()
        move_settings.Speed = int(speed)
        self.axis.set_move_settings_calb(move_settings)

    def set_acceleration(self, *acceleration):
        """
        Sets the acceleration of the Standa device.

        Args:
            acceleration (float, °/s²): The acceleration to set.
        """
        acceleration = acceleration[0]
        move_settings = self.axis.get_move_settings_calb()
        move_settings.Accel = int(acceleration)
        self.axis.set_move_settings_calb(move_settings)

    def set_deceleration(self, *deceleration):
        """
        Sets the deceleration of the Standa device.

        Args:
            deceleration (float, °/s²): The deceleration to set.
        """
        deceleration = deceleration[0]
        move_settings = self.axis.get_move_settings_calb()
        move_settings.Decel = int(deceleration)
        self.axis.set_move_settings_calb(move_settings)

    def get_position(self):
        """
        Gets the current position of the Standa device.

        Returns:
            float, °: The current position.
        """
        position = self.axis.get_position_calb()
        return position.Position

    def get_position_unwrapped(self):
        raise NotImplementedError("This command is not currently implemented.")

    def get_move_settings(self):
        """
        Gets the current movement settings (speed, acceleration, deceleration).

        Returns:
            tuple: The current speed, acceleration, and deceleration settings (°/s, °/s², °/s²).
        """
        move_settings = self.axis.get_move_settings_calb()
        return float(move_settings.Speed), float(move_settings.Accel), float(move_settings.Decel)

    def get_status(self):
        """
        Gets the current status of the Standa device.

        Returns:
            ximc.Status: The status of the device.
        """
        status = self.axis.get_status()
        return status

    def info(self):
        """
        Retrieves information about the Standa device.

        Returns:
            ximc.DeviceInformation: The device information.
        """
        info = self.axis.get_device_information()
        return info

    def set_zero(self):
        """
        Sets the current position of the Standa device as zero.
        """
        self.axis.command_zero()

    def set_current_angle(self):
        raise NotImplementedError("This command is not currently implemented.")

    def set_current_angle_unwrapped(self):
        raise NotImplementedError("This command is not currently implemented.")

    def abort(self):
        """
        Aborts any ongoing movement of the Standa device.
        """
        self.axis.command_sstp()

    def stop(self):
        raise NotImplementedError("This command is not currently implemented.")
