# Smart Greenhouse IoT Project

This is a final project for WES 237A - Embedded System Design at UCSD, showcasing:
- PYNQ Z-2 Board usage
- IoT sensor integration (BME280, BH1750)
- Actuator control (fan, pump, grow light)
- Multitasking with Python threads
- MQTT-based networking

## Setup

1. **Clone the repo** or copy files to your PYNQ board.
2. **Install Python dependencies**:
   ```bash
   sudo pip3 install adafruit-circuitpython-bme280 adafruit-circuitpython-bh1750 paho-mqtt
