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

class Behavior {
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
}

class Robot {
    /**This is the official robot class. API endpoints were organized the
     same way as the python API for Vector.

     All of the api's return Promises
     **/

    constructor() {
        this.behavior = new Behavior()
    }

    // Robot functions
    getBatteryState() {
        return get("/api/robot/get_battery_state")
    }
}

let robot = new Robot();

export default robot