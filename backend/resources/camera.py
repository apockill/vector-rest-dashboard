import cv2
import numpy as np
from anki_vector.robot import Robot
from flask import Response


def camera_stream(robot: Robot):
    while True:
        image = robot.camera.latest_image
        rgb_img = np.array(image)
        bgr_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
        jpg_bytes = cv2.imencode('.jpg', bgr_img)[1].tostring()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n')


def attach(app, robot: Robot):
    @app.route("/api/camera")
    def camera():
        """Return an MJPEG stream with the latest """
        return Response(camera_stream(robot),
                        mimetype='multipart/x-mixed-replace; boundary=frame')
