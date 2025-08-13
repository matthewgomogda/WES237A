"""
smart_greenhouse_main.py
------------------------
Main application entry point for the Smart Greenhouse IoT Project.
"""

import time
import threading
from sensors import SensorManager
from actuators import Actuator
from controller import GreenhouseController
from networking import MQTTClient

def sensor_thread_fn(sensor_mgr, sensor_data_dict, interval=5):
    """
    Background thread to read sensors and update shared dictionary.
    """
    while True:
        readings = sensor_mgr.read_sensors()
        # Update shared data (thread-safe approach recommended in real code)
        sensor_data_dict.update(readings)
        time.sleep(interval)

def controller_thread_fn(controller_obj, sensor_data_dict, interval=2):
    """
    Background thread to run control logic periodically.
    """
    while True:
        # Read sensor data
        data_copy = dict(sensor_data_dict)  # shallow copy
        # Run control step
        controller_obj.control_step(data_copy)
        time.sleep(interval)

def networking_thread_fn(mqtt_client, sensor_data_dict, interval=5):
    """
    Background thread to publish sensor data to MQTT broker.
    """
    mqtt_client.start()
    while True:
        data_copy = dict(sensor_data_dict)
        mqtt_client.publish_sensor_data(data_copy)
        time.sleep(interval)

def main():
    """
    Main function that initializes all components and spawns threads.
    """
    # Shared dictionary for sensor data
    sensor_data = {
        'temperature': 0.0,
        'humidity': 0.0,
        'pressure': 0.0,
        'light': 0.0
    }

    # Initialize Sensors
    sensor_mgr = SensorManager(i2c_bus_id=1, bme280_address=0x76, bh1750_address=0x23)

    # Initialize Actuators
    # You must adjust pin numbers and overlay to match your PYNQ design.
    fan_act = Actuator(pin_number=0)    # Example: Digital out controlling the fan
    pump_act = Actuator(pin_number=1)   # Example: Digital out controlling the pump
    light_act = Actuator(pin_number=2)  # Example: Digital out controlling the light

    # Create Controller
    greenhouse_ctl = GreenhouseController(fan_actuator=fan_act,
                                          pump_actuator=pump_act,
                                          light_actuator=light_act)

    # Setup Networking (MQTT)
    mqtt_client = MQTTClient(broker_host="test.mosquitto.org",
                             broker_port=1883,
                             topic_prefix="smart_greenhouse/teamXX")

    # Start threads
    t_sensor = threading.Thread(target=sensor_thread_fn, args=(sensor_mgr, sensor_data), daemon=True)
    t_controller = threading.Thread(target=controller_thread_fn, args=(greenhouse_ctl, sensor_data), daemon=True)
    t_network = threading.Thread(target=networking_thread_fn, args=(mqtt_client, sensor_data), daemon=True)

    t_sensor.start()
    t_controller.start()
    t_network.start()

    print("Smart Greenhouse System is running. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down system...")

if __name__ == "__main__":
    main()
