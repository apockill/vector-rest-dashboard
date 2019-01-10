import falcon
from anki_vector import Robot, util
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
        requires_behavior_control=True)
    # Connect to the robot and
    robot.connect(robot.behavior_activation_timeout)
    robot.behavior.set_eye_color(0.1, .9)
    robot.behavior.drive_off_charger()
    robot.behavior.drive_straight(distance=util.Distance(distance_mm=10),
                                  speed=util.Speed(100))
    robot.conn.release_control()
    robot.camera.init_camera_feed()
    return robot


def create_app(robot: Robot) -> falcon.API:
    """Initialize the falcon API with all of its routes, and return it."""
    app = falcon.API()
    app.add_error_handler(Exception, generic_error_handler)

    # Create all of the resources
    camera = resources.CameraResource(robot)
    index = resources.IndexResource()
    behavior = resources.BehaviorResource(robot)

    # Create all of the resources
    app.add_static_route(prefix="/", directory=str(STATIC_DIR))
    app.add_route("/api/camera", camera)
    app.add_route("/", index)
    app.add_route("/api/behavior", behavior)

    # Register swagger UI
    register_swaggerui_app(
        app,
        base_url="/docs",
        api_url="/swagger.json",
        page_title="Vector Dashboard Documentation",
        config={"supportedSubmitMethods": ['get', 'put', 'post', 'delete']})

    return app
