from picamera2 import Picamera2
import time

camera = Picamera2()

camera.start()
time.sleep(2)   # let camera adjust exposure

camera.capture_file("picture-office.jpg")

camera.close()
print("Saved picture-office.jpg")