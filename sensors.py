"""
sensors.py
----------
Handles sensor initialization and data acquisition for the Smart Greenhouse Project.
Works with BME280 (temp, humidity, pressure) and BH1750 (lux) via I2C.
"""

import time
import board  # From CircuitPython for I2C
import busio
import adafruit_bme280
import adafruit_bh1750


class SensorManager:
    """
    Manages I2C sensor readings from a BME280 and BH1750.
    """

    def __init__(self, i2c_bus_id=1, bme280_address=0x76, bh1750_address=0x23):
        """
        Initialize I2C bus and sensor objects.

        Parameters:
        -----------
        i2c_bus_id : int
            The I2C bus number on the PYNQ Z-2 (often 0 or 1).
        bme280_address : hex
            I2C address for the BME280 sensor.
        bh1750_address : hex
            I2C address for the BH1750 light sensor.
        """
        self.i2c = busio.I2C(board.SCL, board.SDA)

        # Initialize BME280
        self.bme280 = adafruit_bme280.Adafruit_BME280_I2C(self.i2c, address=bme280_address)
        # Optionally configure oversampling, etc.:
        self.bme280.sea_level_pressure = 1013.25  # Default value

        # Initialize BH1750
        self.bh1750 = adafruit_bh1750.BH1750(self.i2c, address=bh1750_address)

    def read_sensors(self):
        """
        Reads all sensors and returns a dictionary with sensor data.
        """
        data = {}
        # BME280 readings
        data['temperature'] = self.bme280.temperature  # °C
        data['humidity'] = self.bme280.humidity  # %
        data['pressure'] = self.bme280.pressure  # hPa

        # BH1750 reading
        data['light'] = self.bh1750.lux  # lux

        return data

