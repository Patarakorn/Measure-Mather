import os
import time
import queue
from threading import Thread
from gpiozero import DistanceSensor
from picamzero import Camera

from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError

home_dir = os.environ['HOME']
folder = os.path.join(home_dir, "MeasureMather")
os.makedirs(folder, exist_ok=True)

sensor = DistanceSensor(echo=17, trigger=4)

cam = Camera()

plate_number = 1
threshold = 0.2

SCOPES = ['https://www.googleapis.com/auth/drive.file']
creds = Credentials.from_authorized_user_file('token.json', SCOPES)
drive_service = build('drive', 'v3', credentials=creds)

drive_folder_id = "your_drive_folder_id_here"  # Replace with your Google Drive folder ID

upload_queue = queue.Queue()

def uploader():
    """Background thread that uploads files from the queue to Google Drive."""
    while True:
        file_path = upload_queue.get()
        if file_path is None:
            break
        try:
            file_metadata = {'name': os.path.basename(file_path)}
            if drive_folder_id:
                file_metadata['parents'] = [drive_folder_id]
            media = MediaFileUpload(file_path, mimetype='image/jpeg')
            file = drive_service.files().create(
                body=file_metadata,
                media_body=media,
                fields='id'
            ).execute()
            print(f"Uploaded {file_path} to Google Drive with file ID: {file.get('id')}")
            os.remove(file_path)
        except HttpError as error:
            print(f"Failed to upload {file_path}: {error}")
        finally:
            upload_queue.task_done()
            
upload_thread = Thread(target=uploader, daemon=True)
upload_thread.start()

print(f"Waiting for objects within {threshold} meters...")

try:
    while True:
        if sensor.distance < threshold:
            file_path = os.path.join(folder, f"plate_{plate_number}.jpg")
            cam.take_photo(file_path)
            print(f"Captured image: {file_path}")
            upload_queue.put(file_path)
            plate_number += 1
            time.sleep(2)
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Program terminated by user.")
    upload_queue.put(None)