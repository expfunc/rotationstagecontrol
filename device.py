class Device:
    def connect(self, *args):
        raise NotImplementedError("This method should be overridden in a subclass.")

    def disconnect(self):
        raise NotImplementedError("This method should be overridden in a subclass.")

    # Motion commands
    def move_absolute(self, next_position):
        raise NotImplementedError("This method should be overridden in a subclass.")

    def move_relative(self, relative_shift):
        raise NotImplementedError("This method should be overridden in a subclass.")

    # Move settings
    def set_acceleration(self, acceleration):
        raise NotImplementedError("This method should be overridden in a subclass.")

    def set_deceleration(self, deceleration):
        raise NotImplementedError("This method should be overridden in a subclass.")

    def set_speed(self, speed):
        raise NotImplementedError("This method should be overridden in a subclass.")

    # Get current position
    def get_position(self):
        raise NotImplementedError("This method should be overridden in a subclass.")

    def get_move_settings(self):
        raise NotImplementedError("This method should be overridden in a subclass.")

    def get_status(self):
        raise NotImplementedError("This method should be overridden in a subclass.")

    # Set current position as zero
    def set_zero(self):
        raise NotImplementedError("This method should be overridden in a subclass.")

    def abort(self):
        raise NotImplementedError("This method should be overridden in a subclass.")

    def info(self):
        raise NotImplementedError("This method should be overridden in a subclass.")