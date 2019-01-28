import ApiEndpoint from "./endpoint"


class Behavior {
    constructor() {

        this.apiDriveStraight = new ApiEndpoint(
            "/api/robot/behavior/drive_straight");
        this.apiTurnInPlace = new ApiEndpoint(
            "/api/robot/behavior/turn_in_place");
        this.apiSetHeadAngle = new ApiEndpoint(
            "/api/robot/behavior/set_head_angle");
        this.apiSetLiftAngle = new ApiEndpoint(
            "/api/robot/behavior/set_lift_height");
        this.apiDockWithCube = new ApiEndpoint(
            "/api/robot/behavior/dock_with_cube");
        this.apiDriveOnCharger = new ApiEndpoint(
            "/api/robot/behavior/drive_on_charger");
        this.apiDriveOffCharger = new ApiEndpoint(
            "/api/robot/behavior/drive_off_charger");
    }

    // Behavior functions for the robot
    driveStraight = (distance, speed) => (
        this.apiDriveStraight.post({
            distance: distance,
            speed: speed
        })
    );

    turnInPlace = (angle, speed, accel) => (
        this.apiTurnInPlace.post({
            angle: angle,
            speed: speed,
            accel: accel
        })
    );

    setHeadAngle = (angle, accel, maxSpeed, duration) => (
        this.apiSetHeadAngle.post({
            angle: angle,
            accel: accel,
            max_speed: maxSpeed,
            duration: duration
        })
    );

    setLiftHeight = (height, accel, maxSpeed, duration) => (
        this.apiSetLiftAngle.post({
            height: height,
            accel: accel,
            max_speed: maxSpeed,
            duration: duration
        })
    );

    dockWithCube = () => (
        this.apiDockWithCube.post({})
    );

    driveOnCharger = () => (
        this.apiDriveOnCharger.post({})
    );

    driveOffCharger = () => (
        this.apiDriveOffCharger.post({})
    );
}

class Robot {
    /**This is the official robot class. API endpoints were organized the
     same way as the python API for Vector.

     All of the api's return Promises
     **/

    constructor() {
        // Keep track of API calls and prevent multiple calls for the same API
        // at the same time.
        this.behavior = new Behavior();
        this.apiGetBatteryState = new ApiEndpoint(
            "/api/robot/get_battery_state");
    }

    // Base Robot functions
    getBatteryState = () => (
        this.apiGetBatteryState.get()
    )
}

let robot = new Robot();

export default robot