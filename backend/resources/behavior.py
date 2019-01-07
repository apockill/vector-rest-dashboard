# from enum import Enum
#
# from anki_vector.robot import Robot
# from flask_restplus import Resource, fields, marshal_with, Api
#
#
# class Action(Enum):
#     drive_off_charger = "drive_off_charger"
#     drive_on_charger = "drive_on_charger"
#     dock_with_cube = "dock_with_cube"
#     drive_straight = "drive_straight"
#     turn_in_place = "turn_in_place"
#     set_head_angle = "set_head_angle"
#     set_lift_height = "set_lift_height"
#
#
# class BehaviorModel:
#     resource_fields = {
#         "action": fields.String(
#
#             description="The action to perform",
#             enum=[Action._member_names_]),
#     }
#
#
# class Behavior(Resource):
#     def __init__(self, **kwargs):
#       pass
#
#     @api.doc(
#         notes="Perform an action with the robot",
#         nickname="Behavior",
#         parameters=[
#             {
#                 "name": "body",
#                 "description": "Action that needs to be performed",
#                 "required": True,
#                 "allowMultiple": False,
#                 "dataType": BehaviorModel.__name__
#             }
#         ],
#         responseMessages=[
#             {
#                 "code": 201,
#                 "message": "Action Performed."
#             },
#             {
#                 "code": 400,
#                 "message": "Unknown behavior type!"
#             }
#         ]
#     )
#     @marshal_with(BehaviorModel.resource_fields)
#     def get(self):
#         return {"it worked!": "ayy lmao\ntest"}
#
#
# def attach(api: Api, robot: Robot):
#     """
#     Different actions:
#         - drive_off_charger
#         - drive_on_charger
#         - dock_with_cube
#             target_object
#             approach_angle
#             alignment_type
#             distance_from_marker
#             num_retries
#         - drive_straight
#             distance
#             speed
#             should_play_anim (t/f)
#             num_retries
#         - turn_in_place
#             angle
#             speed
#             accel
#             angle_tolerance
#             is_absolute
#             num_retries
#         - set_head_angle
#             angle
#             accel
#             max_speed
#             duration
#             num_retries
#         - set_lift_height
#             height
#             accel
#             max_speed
#             duration
#             num_retries
#     """
#     api.add_resource(Behavior, "/api/behavior",
#                      resource_class_kwargs={"smart_engine": 69.420})
