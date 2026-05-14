# Imports
import time
import board
import adafruit_dht

# Setup
dhtDevice = adafruit_dht.DHT11(board.D5)

# Activate
def activate():
    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9/5) + 32
        humidity = dhtDevice.humidity
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        temperature_c = 0
        temperature_f = 0
        humidity = 0
    return temperature_c, temperature_f, humidity
    

# Destroy
def destroy():
    dhtDevice.exit()