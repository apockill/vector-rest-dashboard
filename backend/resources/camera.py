from threading import RLock
from time import sleep

import cv2
import numpy as np
from PIL import Image
from anki_vector.robot import Robot


class CameraResource:
    def __init__(self, robot: Robot):
        self.robot = robot
        self.stream = self._stream_generator()

        # Create a cache so as to not hit the robot object so hard
        self._last_image: Image = None

        # Create a cache of the last sent stream packet
        self._last_packet = None
        self._last_packet_lock = RLock()

    def _stream_generator(self):
        """A generator that yields byte frame packets for an MJPEG stream.
        It is designed to limit checks and calls to the robot, and cache
        every frame sent (in case there are multiple clients connected). """
        last_sent_image = None

        while True:
            image = self.robot.camera.latest_image
            sleep(.025)  # Limit checks to 40 times per second

            # Only send frames when there's a new frame
            if last_sent_image == image:
                continue

            # Only one client should use the cache at a time
            with self._last_packet_lock:
                last_sent_image = image
                if self._last_image == image:
                    yield self._last_packet
                    continue

                rgb_img = np.array(image)
                bgr_img = cv2.cvtColor(rgb_img, cv2.COLOR_RGB2BGR)
                jpg_bytes = cv2.imencode('.jpg', bgr_img)[1].tostring()

                # Cache the packet and its image
                self._last_image = image
                self._last_packet = \
                    (b'--frame\r\n'
                     b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n')

                yield self._last_packet

    def on_get(self, req, resp):
        resp.content_type = 'multipart/x-mixed-replace; boundary=frame'
        resp.stream = self._stream_generator()
