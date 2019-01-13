import falcon
from anki_vector import Robot, objects
from anki_vector.util import Speed, Distance, Angle
from falcon import Request, Response

from backend.open_api_validator import validator

"""
Different actions:
    # Implemented
    - drive_off_charger
    - drive_on_charger
    - dock_with_cube
        target_object
        approach_angle
        alignment_type
        distance_from_marker
        num_retries
    - drive_straight
        distance
        speed
        should_play_anim (t/f)
        num_retries
    - turn_in_place
        angle
        speed
        accel
        angle_tolerance
        is_absolute
        num_retries
        
        
    - set_head_angle
        angle
        accel
        max_speed
        duration
        num_retries
    - set_lift_height
        height
        accel
        max_speed
        duration
        num_retries
"""


class BehaviorResource:
    def __init__(self, robot: Robot):
        self.robot: Robot = robot


@falcon.before(validator)
class DriveOnCharger(BehaviorResource):
    def on_post(self, req: Request, resp: Response, **validated):
        self.robot.behavior.drive_on_charger()
        resp.body = "true"


@falcon.before(validator)
class DriveOffCharger(BehaviorResource):
    def on_post(self, req: Request, resp: Response, **validated):
        self.robot.behavior.drive_off_charger()
        resp.body = "true"


@falcon.before(validator)
class DockWithCube(BehaviorResource):
    def on_post(self, req: Request, resp: Response, **validated):
        self.robot.behavior.dock_with_cube(
            target=objects.LightCube,
            approach_angle=None,
            num_retries=0)
        resp.body = "true"


@falcon.before(validator)
class DriveStraight(BehaviorResource):
    def on_post(self, req: Request, resp: Response, **validated):
        self.robot.behavior.drive_straight(
            distance=Distance(distance_mm=validated["distance"]),
            speed=Speed(speed_mmps=validated["speed"]),
            should_play_anim=False)
        resp.body = "true"


@falcon.before(validator)
class TurnInPlace(BehaviorResource):
    def on_post(self, req: Request, resp: Response, **validated):
        self.robot.behavior.turn_in_place(
            angle=Angle(radians=validated["angle"]),
            speed=Angle(radians=validated["speed"]),
            accel=Angle(radians=validated["accel"]))
        resp.body = "true"


@falcon.before(validator)
class SetHeadAngle(BehaviorResource):
    def on_post(self, req: Request, resp: Response, **validated):
        self.robot.behavior.set_head_angle(
            angle=Angle(radians=validated["angle"]),
            max_speed=validated["max_speed"],
            accel=validated["accel"],
            duration=validated["duration"])