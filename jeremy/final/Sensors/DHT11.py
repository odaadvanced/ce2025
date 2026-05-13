# Imports
import time
import board
import adafruit_dht

# Setup
dhtDevice = adafruit_dht.DHT11(board.D5)

# Activate
def activate():
    temperature_c = dhtDevice.temperature
    temperature_f = temperature_c * (9/5) + 32
    humidity = dhtDevice.humidity
    return temperature_c, temperature_f, humidity

# Destroy
def destroy():
    dhtDevice.exit()