import scrcpy
from adbutils import adb
import adbutils
import cv2


try:
    adb = adbutils.AdbClient(host="10.122.84.85", port=8000, socket_timeout=10)
    client = scrcpy.Client(device=adb.device_list()[0])
except Exception as e:
    print("Connection failed:", str(e))

def on_frame(frame):
    # If you set non-blocking (default) in constructor, the frame event receiver 
    # may receive None to avoid blocking event.
    if frame is not None:
        # frame is an bgr numpy ndarray (cv2' default format)
        cv2.imshow("viz", frame)
        cv2.waitKey(10)

client.add_listener(scrcpy.EVENT_FRAME, on_frame)
client.start(threaded=True)