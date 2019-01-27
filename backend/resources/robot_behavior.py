import falcon
from anki_vector.util import Speed, Distance, Angle
from falcon import Request, Response, errors

from backend.open_api_validator import validator
from .robot import RobotResource


@falcon.before(validator)
class DriveOnCharger(RobotResource):
    def on_post(self, req: Request, resp: Response, **validated):
        self.robot.behavior.drive_on_charger()
        resp.body = "true"


@falcon.before(validator)
class DriveOffCharger(RobotResource):
    def on_post(self, req: Request, resp: Response, **validated):
        self.robot.behavior.drive_off_charger()
        resp.body = "true"


@falcon.before(validator)
class DockWithCube(RobotResource):
    def on_post(self, req: Request, resp: Response, **validated):
        self.robot.world.connect_cube()
        light_cube = self.robot.world.connected_light_cube
        print("Got light_cube", light_cube)
        if light_cube:
            dock_response = self.robot.behavior.dock_with_cube(
                target_object=light_cube,
                approach_angle=None,
                num_retries=0)
            print("Tried docking, ", dock_response)
        else:
            raise errors.HTTPInternalServerError(
                title="Action Failed",
                description="Unable to connect to lightcube!")
        resp.body = "true"


@falcon.before(validator)
class DriveStraight(RobotResource):
    def on_post(self, req: Request, resp: Response, **validated):
        self.robot.behavior.drive_straight(
            distance=Distance(distance_mm=validated["distance"]),
            speed=Speed(speed_mmps=validated["speed"]),
            should_play_anim=False)
        resp.body = "true"


@falcon.before(validator)
class TurnInPlace(RobotResource):
    def on_post(self, req: Request, resp: Response, **validated):
        self.robot.behavior.turn_in_place(
            angle=Angle(radians=validated["angle"]),
            speed=Angle(radians=validated["speed"]),
            accel=Angle(radians=validated["accel"]))
        resp.body = "true"


@falcon.before(validator)
class SetHeadAngle(RobotResource):
    def on_post(self, req: Request, resp: Response, **validated):
        self.robot.behavior.set_head_angle(
            angle=Angle(radians=validated["angle"]),
            max_speed=validated["max_speed"],
            accel=validated["accel"],
            duration=validated["duration"])
        resp.body = "true"


@falcon.before(validator)
class SetLiftHeight(RobotResource):
    def on_post(self, req: Request, resp: Response, **validated):
        self.robot.behavior.set_lift_height(
            height=validated["height"],
            accel=validated["accel"],
            max_speed=validated["max_speed"],
            duration=validated["duration"])
        resp.body = "true"
