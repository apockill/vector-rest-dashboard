from enum import Enum

import falcon

from backend.open_api_validator import validator


class Action(Enum):
    drive_off_charger = "drive_off_charger"
    drive_on_charger = "drive_on_charger"
    dock_with_cube = "dock_with_cube"
    drive_straight = "drive_straight"
    turn_in_place = "turn_in_place"
    set_head_angle = "set_head_angle"
    set_lift_height = "set_lift_height"


@falcon.before(validator)
class BehaviorResource:
    """
    Different actions:
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

    def __init__(self, robot):
        self.robot = robot

    def on_get(self):
        pass
