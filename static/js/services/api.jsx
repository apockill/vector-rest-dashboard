// Helpers
function post(endpoint, body) {
    return fetch(endpoint, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(body)
    }).then(res => res.json())
}

function get(endpoint) {
    return fetch(endpoint).then(res => res.json())
}

class ApiEndpoing {
    constructor(url) {

    }

}

class Behavior {
    constructor() {
        this.apiState = {
            driveStraight: false,
            turnInPlace: false,
            setHeadAngle: false,
            setLiftHeight: false,
            dockWithCube: false,
            driveOnCharger: false,
            driveOffCharger: false
        }
    }

    // Behavior functions for the robot
    driveStraight(distance, speed) {
        return post("/api/robot/behavior/drive_straight", {
            distance: distance,
            speed: speed
        })
    }

    turnInPlace(angle, speed, accel) {
        return post("/api/robot/behavior/turn_in_place", {
            angle: angle,
            speed: speed,
            accel: accel
        })
    }

    setHeadAngle(angle, accel, maxSpeed, duration) {
        return post("/api/robot/behavior/set_head_angle", {
            angle: angle,
            accel: accel,
            max_speed: maxSpeed,
            duration: duration
        })
    }

    setLiftHeight(height, accel, maxSpeed, duration) {
        return post("/api/robot/behavior/set_lift_height", {
            height: height,
            accel: accel,
            max_speed: maxSpeed,
            duration: duration
        })
    }

    dockWithCube() {
        return post("/api/robot/behavior/dock_with_cube", {})
    }

    driveOnCharger() {
        return post("/api/robot/behavior/drive_on_charger", {})
    }

    driveOffCharger() {
        return post("/api/robot/behavior/drive_off_charger", {})
    }
}

class Robot {
    /**This is the official robot class. API endpoints were organized the
     same way as the python API for Vector.

     All of the api's return Promises
     **/

    constructor() {
        // Keep track of API calls and prevent multiple calls for the same API
        // at the same time.
        this.apiState = {
            getBatteryState: false,
        }

        this.behavior = new Behavior()
    }

    // Base Robot functions
    getBatteryState() {
        return get("/api/robot/get_battery_state")
    }
}

let robot = new Robot();

export default robot