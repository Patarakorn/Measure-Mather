import os
import time
from gpiozero import DistanceSensor
from picamzero import Camera

home_dir = os.environ['HOME']
folder = os.path.join(home_dir, "MeasureMather")
os.makedirs(folder, exist_ok=True)

sensor = DistanceSensor(echo=17, trigger=4)

cam = Camera()

plate_number = 1
threshold = 0.2

print(f"Waiting for objects within {threshold} meters...")

try:
    while True:
        if sensor.distance < threshold:
            file_path = os.path.join(folder, f"plate_{plate_number}.jpg")
            cam.take_photo(file_path)
            print(f"Captured Image: {file_path}")
            
            plate_number += 1
            time.sleep(2)
            
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program terminated by user.")