import ujson

import falcon
from google.protobuf.json_format import MessageToDict
from anki_vector import Robot
from falcon import Request, Response

from backend.open_api_validator import validator


class RobotResource:
    def __init__(self, robot: Robot):
        self.robot: Robot = robot


@falcon.before(validator)
class GetBatteryState(RobotResource):
    def on_get(self, req: Request, resp: Response, **validated):
        battery_response = self.robot.get_battery_state()
        resp_dict = {
            "battery_level": battery_response.batteryLevel,
            "battery_volts": battery_response.batteryVolts,
            "is_charging": battery_response.isCharging,
            "is_on_charger_platform": battery_response.is_on_charger_platform,
            "suggested_charger_sec": battery_response.suggestedChargerSec
        }
        print("Battery info", resp_dict)
        resp.body = ujson.dumps(resp_dict)
