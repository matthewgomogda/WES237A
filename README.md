# WES237A FINAL PROJECT

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
3. **Wire up hardware as documented**:
- Sensors on I2C pins
- Actuators on GPIO pins with external power

4. **Run the application:**

```bash
cd smart_greenhouse
python3 smart_greenhouse_main.py
