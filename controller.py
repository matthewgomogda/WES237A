"""
controller.py
-------------
Implements the control logic for the Smart Greenhouse.
"""

import time

class GreenhouseController:
    """
    Contains logic to control environmental conditions
    (fan, pump, lights) based on sensor readings.
    """

    def __init__(self, fan_actuator=None, pump_actuator=None, light_actuator=None):
        """
        Store references to actuator objects.
        """
        self.fan_actuator = fan_actuator
        self.pump_actuator = pump_actuator
        self.light_actuator = light_actuator

        # Define default thresholds (customize as needed)
        self.max_temperature = 30.0  # °C
        self.min_humidity = 40.0     # %
        self.min_light = 200.0       # lux (example threshold)

    def control_step(self, sensor_data):
        """
        Perform one control cycle using the sensor readings.
        sensor_data : dict
            e.g. { 'temperature': 25.3, 'humidity': 45.2, 'light': 150.0 }
        """
        temp = sensor_data.get('temperature', 25.0)
        hum = sensor_data.get('humidity', 45.0)
        lux = sensor_data.get('light', 300.0)

        # Control Fan based on temperature
        if temp > self.max_temperature:
            if self.fan_actuator:
                self.fan_actuator.turn_on()
        else:
            if self.fan_actuator:
                self.fan_actuator.turn_off()

        # Control Pump based on humidity (simple example)
        if hum < self.min_humidity:
            if self.pump_actuator:
                self.pump_actuator.turn_on()
        else:
            if self.pump_actuator:
                self.pump_actuator.turn_off()

        # Control Light if ambient light is too low
        if lux < self.min_light:
            if self.light_actuator:
                self.light_actuator.turn_on()
        else:
            if self.light_actuator:
                self.light_actuator.turn_off()
