import scrcpy
from adbutils import adb 
import cv2

adb.connect("10.122.84.85:22614")
client = scrcpy.Client(device=adb.device_list()[0])

def on_frame(frame):
    # If you set non-blocking (default) in constructor, the frame event receiver 
    # may receive None to avoid blocking event.
    if frame is not None:
        # frame is an bgr numpy ndarray (cv2' default format)
        cv2.imshow("viz", frame)
    cv2.waitKey(10)

client.add_listener(scrcpy.EVENT_FRAME, on_frame)