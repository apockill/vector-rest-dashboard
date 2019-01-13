from argparse import ArgumentParser
from pathlib import Path

from backend import server

CERT_DIR = Path.home() / ".anki_vector"


def parse_args():
    parser = ArgumentParser(
        description="Run a webserver and control your vector!")
    parser.add_argument("--cert-filename", type=Path, default=None,
                        help="File name of your vectors certificate. You can"
                             " find this under ~/.anki_vector/Vector-*-.cert")
    parser.add_argument("--hostname", type=str, default="0.0.0.0",
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


def start_app():
    """
    The purpose of this function is to
        - handle arguments for the server
        - Set up "environment objects" and services, such as the robot
        - Pass these into "create_app" to get the app, and return it
    This makes it easy to test "create_app" because we can pass different
    mocked objects into it."""

    # Get args
    args = parse_args()
    cert_path = CERT_DIR / args.cert_filename

    # Create the robot
    robot = server.create_robot(cert_path=cert_path)

    # Create a function for gracefully closing app state
    def close_app():
        print("Server has started closing...")
        robot.disconnect()
        print("Server has closed cleanly!")

    # Register the function to uwsgi's atexit functionality
    try:
        import uwsgi
        uwsgi.atexit = close_app
    except ModuleNotFoundError:
        print("Not running in uWSGI mode")

    app = server.create_app(robot)
    return app


app = start_app()
