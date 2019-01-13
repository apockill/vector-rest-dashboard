from time import sleep

import falcon
from anki_vector import Robot
from anki_vector.exceptions import VectorNotFoundException
from falcon_swagger_ui import register_swaggerui_app

from backend import resources, STATIC_DIR


def generic_error_handler(ex: Exception, req, resp, params):
    """Handles uncaught exceptions in a format that is consistent with the rest
    of Falcon's error handling.
    """
    if isinstance(ex, falcon.HTTPError):
        # Use Falcon's built-in error handling for HTTPErrors
        raise ex

    print("Uncaught exception", exc_info=ex)
    raise falcon.HTTPInternalServerError(
        title=type(ex),
        description=str(ex))


def create_robot(cert_path: str) -> Robot:
    """
    :param cert_path: Path to the vector certificate (for connecting)
    """
    robot = Robot(
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
        requires_behavior_control=False)

    # Continuously try to connect to the robot
    while True:
        try:
            robot.connect(robot.behavior_activation_timeout)
            break
        except VectorNotFoundException:
            print("Unable to connect to Vector! Trying again...")

    # Check if the robot is charged
    battery_charge_time_left = robot.get_battery_state().suggested_charger_sec
    while battery_charge_time_left > 0:
        print(f"Charging: {battery_charge_time_left} seconds left...")
        battery_charge_time_left = robot.get_battery_state().suggested_charger_sec
        sleep(1)

    # Get control and move a little, so as to build a map (seems to help bugs?)
    robot.conn.request_control()
    robot.behavior.set_eye_color(0.1, .9)

    robot.camera.init_camera_feed()
    return robot


def create_app(robot: Robot) -> falcon.API:
    """Initialize the falcon API with all of its routes, and return it."""
    app = falcon.API()
    app.add_error_handler(Exception, generic_error_handler)

    # Create all of the resources
    camera = resources.CameraResource(robot)
    index = resources.IndexResource()

    # Create all of the resources
    app.add_static_route(prefix="/", directory=str(STATIC_DIR))
    app.add_route("/api/camera", camera)
    app.add_route("/", index)
    app.add_route("/api/behavior/drive_off_charger",
                  resources.DriveOffCharger(robot))
    app.add_route("/api/behavior/drive_on_charger",
                  resources.DriveOnCharger(robot))
    app.add_route("/api/behavior/dock_with_cube",
                  resources.DockWithCube(robot))
    app.add_route("/api/behavior/drive_straight",
                  resources.DriveStraight(robot))
    app.add_route("/api/behavior/turn_in_place",
                  resources.TurnInPlace(robot))
    app.add_route("/api/behavior/set_head_angle",
                  resources.SetHeadAngle(robot))

    # Register swagger UI
    register_swaggerui_app(
        app,
        base_url="/docs",
        api_url="/swagger.json",
        page_title="Vector Dashboard Documentation",
        config={"supportedSubmitMethods": ['get', 'put', 'post', 'delete']})

    return app
