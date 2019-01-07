import cv2
import numpy as np
from anki_vector.robot import Robot

class CameraResource:
    def __init__(self, robot: Robot):
        self.robot = robot

    def stream(self):
        while True:
            image = self.robot.camera.latest_image
            rgb_img = np.array(image)
            bgr_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
            jpg_bytes = cv2.imencode('.jpg', bgr_img)[1].tostring()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n')

    def on_get(self, req, resp):
        resp.content_type = 'multipart/x-mixed-replace; boundary=frame'
        resp.stream = self.stream()