# Imports !!
import sys
import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

import RPi.GPIO as GPIO
import asyncio

from Sensors import Photoresistor, DHT11, PhotographModule

from sphero_sdk import SpheroRvrAsync
from sphero_sdk import SerialAsyncDal
import time

# Setup stuff
loop = asyncio.get_event_loop()
rvr = SpheroRvrAsync(
    dal=SerialAsyncDal(
        loop
        )
    )
GPIO.setmode(GPIO.BCM)

right_trigger = 25
right_echo = 12
left_trigger = 23
left_echo = 24

GPIO.setup(left_trigger, GPIO.OUT)
GPIO.setup(left_echo, GPIO.IN)
GPIO.setup(right_trigger, GPIO.OUT)
GPIO.setup(right_echo, GPIO.IN)

Photoresistor.setup()
PhotographModule.setup()

# Find distance with the left ultrasonic sensor
def distance_left():
    GPIO.output(left_trigger, True)
    
    time.sleep(0.00001)
    GPIO.output(left_trigger, False)
    
    start_time = time.time()
    stop_time = time.time()
    
    while GPIO.input(left_echo) == 0:
        start_time = time.time()
    
    while GPIO.input(left_echo) == 1:
        stop_time = time.time()
    
    time_elapsed = stop_time - start_time
    
    distance = (time_elapsed * 34300) / 2
    return distance

# Find distance with the right ultrasonic sensor
def distance_right():
    GPIO.output(right_trigger, True)
    
    time.sleep(0.00001)
    GPIO.output(right_trigger, False)
    
    start_time = time.time()
    stop_time = time.time()
    
    while GPIO.input(right_echo) == 0:
        start_time = time.time()
    
    while GPIO.input(right_echo) == 1:
        stop_time = time.time()
    
    time_elapsed = stop_time - start_time
    
    distance = (time_elapsed * 34300) / 2
    return distance

# Main function
async def main():
    await rvr.wake()
    await rvr.reset_yaw()
    await asyncio.sleep(.5)
    
    # Variables
    average_temp = 0
    total_temp = 0
    count = 0
    dark_count = 0
    light_count = 0
    
    # Loop !!
    while True:
        dist_r = distance_right()
        dist_l = distance_left()
        await asyncio.sleep(.05)
        
        # Print
        print('Measurements are {0} cm right and {1} cm left'.format(dist_r, dist_l))
        
        # Cool visual stuff
        if dist_r >= 200 or dist_l >= 200:
            await rvr.led_control.set_all_leds_rgb(red=0, green=255, blue=0)
        elif dist_r >= 100 or dist_l >= 100:
            await rvr.led_control.set_all_leds_rgb(red=255, green=255, blue=0)
        elif dist_r >= 35 or dist_l >= 35:
            await rvr.led_control.set_all_leds_rgb(red=255, green=100, blue=0)
            
        # Turning
        if dist_r < 35:
            while dist_r < 35:
                await rvr.raw_motors(2,125,1,125)
                dist_r = distance_right()
                await asyncio.sleep(.05)
                print('turning right')
                await rvr.led_control.set_all_leds_rgb(red=255, green=0, blue=0)
            await rvr.reset_yaw()
        elif dist_l < 35:
            while dist_l < 35:
                await rvr.raw_motors(1,125,2,125)
                dist_l = distance_left()
                await asyncio.sleep(.05)
                print('turning left')
                await rvr.led_control.set_all_leds_rgb(red=255, green=0, blue=0)
            await rvr.reset_yaw()
        elif dist_l >= 35 and dist_r >= 35:
            await rvr.drive_with_heading(50,0,0)
        
        # Boolean :fire:
        is_env_odd = False
        
        analogVal = Photoresistor.activate()
        temp_c, temp_f, humidity = DHT11.activate()
        
        # Cycle counting
        count = count + 1
        
        # Photoresistor stuff
        if analogVal == 0:
            if light_count >= 5:
                print("Light has changed!")
                is_env_odd = True
            
            dark_count = dark_count + 1
            light_count = 0
        else:
            if dark_count >= 5:
                print("Light has changed!")
                is_env_odd = True
            
            light_count = light_count + 1
            dark_count = 0
        
        # DHT-11 stuff
        total_temp = total_temp + temp_c
        average_temp = total_temp / count
        
        if temp_c > average_temp * 1.25:
            print("Temperature is hotter than usual!")
            is_env_odd = True
        elif temp_c < average_temp / 1.25:
            print("Temperaute is colder than usual!")
            is_env_odd = True
        
        # photo taking
        if is_env_odd == True:
            PhotographModule.activate()

# Activation
try:
    loop.run_until_complete(
        asyncio.gather(
            main()
            )
        )
# Destroy EVERYTHING!!!
except KeyboardInterrupt:
    print('Program ended by KeyboardInterrupt')
    Photoresistor.destroy()
    DHT11.destroy()
    PhotographModule.destroy()
    GPIO.cleanup()