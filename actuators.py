"""
actuators.py
------------
Handles actuator control (Fan, Pump, Light) via GPIO.
"""

import pynq.lib
from pynq.overlays.base import BaseOverlay


class Actuator:
    """
    Generic actuator class for controlling a single digital output.
    """

    def __init__(self, pin_number, overlay_path='base.bit', default_state=False):
        """
        Initialize the GPIO pin for the actuator.

        Parameters:
        -----------
        pin_number : int
            The pin index or channel used by the overlay for the GPIO.
        overlay_path : str
            Path to the bitstream overlay to load.
        default_state : bool
            Initial output state (False = off, True = on).
        """

        # Load the base overlay which provides the pins. Adjust as needed for your design.
        self.overlay = BaseOverlay(overlay_path)
        self.gpio = AxiGPIO(self.overlay.ip_dict['axi_gpio_0']).channel1

        self.pin_mask = 1 << pin_number
        current_value = self.gpio.read()
        # If default_state = True, set the bit in the output
        if default_state:
            self.gpio.write(current_value | self.pin_mask)
        else:
            self.gpio.write(current_value & ~self.pin_mask)

    def turn_on(self):
        """Set the GPIO pin high for this actuator."""
        current_value = self.gpio.read()
        self.gpio.write(current_value | self.pin_mask)

    def turn_off(self):
        """Set the GPIO pin low for this actuator."""
        current_value = self.gpio.read()
        self.gpio.write(current_value & ~self.pin_mask)

    def set_state(self, state):
        """Set the actuator to a boolean state."""
        if state:
            self.turn_on()
        else:
            self.turn_off()

