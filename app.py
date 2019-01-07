import logging
from argparse import ArgumentParser
from pathlib import Path

from anki_vector.robot import Robot

from backend import resources

CERT_DIR = Path.home() / ".anki_vector"


def initialize_app():
    # Parse args
    args = parse_args()
    cert_path = CERT_DIR / args.cert_filename

    logging.basicConfig(level=logging.DEBUG)

    # Create the Flask app
    app = Flask(__name__,
                static_folder="static/dist",
                template_folder="static")

    # Create the api (for rest stuff)
    api = Api(app, version="0.1.")

    # Connect to the robot
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

        # Attach all resources
        resources.index.attach(app)
        resources.camera.attach(app, robot)
        # resources.behavior.attach(api, robot)
        # Attach all flask_restful resources

        # Run the server
        app.run(host='0.0.0.0', port=5000, threaded=True)

    logging.info("Server Closed")


def parse_args():
    parser = ArgumentParser(
        description="Run a webserver and control your vector!")
    parser.add_argument("--cert-filename", type=Path, default=None,
                        help="File name of your vectors certificate. You can"
                             " find this under ~/.anki_vector/Vector-*-.cert")

    args = parser.parse_args()

    # Try to find the vector certificate file
    certs = list(CERT_DIR.glob("Vector*.cert"))
    if len(certs) > 1 and args.cert_filename is None:
        raise EnvironmentError(
            f"You have more than one vector under {str(CERT_DIR)},"
            f" please specify the cert file using --cert-file. "
            f" Your options are: {','.join([str(p.name) for p in certs])}")
    elif len(certs) == 0:
        raise EnvironmentError(
            "You have never set up your vector sdk ! To do this, you must"
            " follow the directions on the readme and run:\n"
            "> py -3 -m pip install anki_vector\n"
            "> py -m anki_vector.configure")

    # Choose the only cert if it is not specified
    if args.cert_filename is None:
        args.cert_filename = certs[0]

    # If the specified cert doesn't exist on the system, throw an error
    if args.cert_filename not in certs:
        raise EnvironmentError(
            f"The chosen vector certificate {args.cert_filename} was not found"
            f" in the cert directory, {CERT_DIR}.")

    return args


if __name__ == "__main__":
    initialize_app()
