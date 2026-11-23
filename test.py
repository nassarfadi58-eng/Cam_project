import cv2
import os

print("OpenCV version:", cv2.__version__)

path = cv2.data.haarcascades

print("Cascade directory:", path)

files = [
    "haarcascade_frontalface_default.xml",
    "haarcascade_eye.xml",
    "haarcascade_smile.xml"
]

for file in files:
    full_path = os.path.join(path, file)

    print(file, ":", os.path.exists(full_path))