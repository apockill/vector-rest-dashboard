import ujson

import falcon
from anki_vector import Robot
from falcon import Request, Response
from google.protobuf.json_format import MessageToDict

from backend.open_api_validator import validator


class RobotResource:
    def __init__(self, robot: Robot):
        self.robot: Robot = robot


@falcon.before(validator)
class GetBatteryState(RobotResource):
    def on_get(self, req: Request, resp: Response, **validated):
        # Get the current battery status
        battery_response = self.robot.get_battery_state()

        # Get it as a dict so we can get string contstants for 'batteryLevel'
        protoc_dict = MessageToDict(battery_response)
        resp_dict = {
            "battery_level": protoc_dict["batteryLevel"],
            "battery_volts": battery_response.battery_volts,
            "is_charging": battery_response.is_charging,
            "is_on_charger_platform": battery_response.is_on_charger_platform,
            "suggested_charger_sec": battery_response.suggested_charger_sec
        }
        resp.body = ujson.dumps(resp_dict)
