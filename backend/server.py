import falcon
import logging
from anki_vector import Robot

from backend import resources, STATIC_DIR


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


def init_app(robot: Robot) -> falcon.API:
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

    return app
