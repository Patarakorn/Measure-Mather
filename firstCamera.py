from picamzero import Camera
import os

home_dir = os.environ['HOME']
cam = Camera()
cam.start_preview()
cam.take_photo(f"{home_dir}/MeasureMather/new_image.jpg")
cam.stop_preview()                                                   