import logging
from argparse import ArgumentParser
from pathlib import Path
from wsgiref import simple_server

from anki_vector import Robot

from backend.server import init_app

CERT_DIR = Path.home() / ".anki_vector"


def parse_args():
    parser = ArgumentParser(
        description="Run a webserver and control your vector!")
    parser.add_argument("--cert-filename", type=Path, default=None,
                        help="File name of your vectors certificate. You can"
                             " find this under ~/.anki_vector/Vector-*-.cert")
    parser.add_argument("--hostname", type=str, default="localhost",
                        help="Hostname for the server to be hosted on")
    parser.add_argument("--port", type=int, default=5000,
                        help="Port for the server to be hosted on")
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


def start_server():
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
        httpd = simple_server.make_server(args.hostname, args.port, app)
        httpd.serve_forever()


if __name__ == "__main__":
    start_server()
