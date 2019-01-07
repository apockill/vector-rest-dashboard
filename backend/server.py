


def init_app(robot: Robot):
    app = falcon.API()
    app.add_error_handler(Exception, generic_error_handler)
    camera = CameraResource(robot)

    # Create all of the resources
    app.add_route("/api/camera", camera)
    return app