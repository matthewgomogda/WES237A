"""
networking.py
-------------
Implements MQTT networking for the Smart Greenhouse.
"""

import time
import json
import threading
import paho.mqtt.client as mqtt

class MQTTClient:
    """
    Simple MQTT client to publish sensor data and subscribe to control commands.
    """

    def __init__(self, broker_host="test.mosquitto.org", broker_port=1883, topic_prefix="smart_greenhouse/teamXX"):
        """
        Initialize MQTT client and connect to broker.
        """
        self.client = mqtt.Client()
        self.broker_host = broker_host
        self.broker_port = broker_port
        self.topic_sensor = f"{topic_prefix}/sensor_data"
        self.topic_control = f"{topic_prefix}/control"
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message

    def on_connect(self, client, userdata, flags, rc):
        print(f"MQTT connected with result code {rc}")
        # Subscribe to control topic if you want to receive commands
        client.subscribe(self.topic_control)

    def on_message(self, client, userdata, msg):
        print(f"Received message on {msg.topic}: {msg.payload}")
        # Parse incoming control commands if needed

    def start(self):
        """
        Start the MQTT client in a separate thread.
        """
        self.client.connect(self.broker_host, self.broker_port, 60)
        thread = threading.Thread(target=self.client.loop_forever, daemon=True)
        thread.start()

    def publish_sensor_data(self, sensor_data):
        """
        Publish sensor data to the sensor topic in JSON format.
        """
        payload = json.dumps(sensor_data)
        self.client.publish(self.topic_sensor, payload)
