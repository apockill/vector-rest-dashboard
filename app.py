import logging
from pathlib import Path
from wsgiref import simple_server

import cv2
import falcon
import numpy as np
from anki_vector import Robot

from app import parse_args

CERT_DIR = Path.home() / ".anki_vector"


def generic_error_handler(ex: Exception, req, resp, params):
    """Handles uncaught exceptions in a format that is consistent with the rest
    of Falcon's error handling.
    """
    if isinstance(ex, falcon.HTTPError):
        # Use Falcon's built-in error handling for HTTPErrors
        raise ex

    logging.critical("Uncaught exception", exc_info=ex)
    raise falcon.HTTPInternalServerError(
        title=type(ex),
        description=str(ex))



def main():
    # Get args
    args = parse_args()
    cert_path = CERT_DIR / args.cert_filename

    # Set logging settings
    logging.basicConfig(level=logging.DEBUG)

    with Robot(
            config={"cert": cert_path},
            default_logging=False,
            cache_animation_list=True,
            enable_face_detection=False,
            enable_camera_feed=True,
            enable_audio_feed=False,
            enable_custom_object_detection=False,
            enable_nav_map_feed=False,
            show_viewer=False,
            show_3d_viewer=False,
            requires_behavior_control=True) as robot:
        robot.behavior.set_eye_color(0.1, .9)
        robot.behavior.drive_off_charger()
        robot.conn.release_control()
        robot.camera.init_camera_feed()

        app = init_app(robot)

        logging.info("Starting Server!")
        httpd = simple_server.make_server("localhost", 5001, app)
        httpd.serve_forever()


if __name__ == "__main__":
    main()
