// Helpers
function post(endpoint, body) {
    return fetch(`/api/${endpoint}`, {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(body)
    }).then(res => res.json())
}

function get(endpoint) {
    return fetch(`/api/${endpoint}`).then(res => res.json())
}

class Behavior {
    // Behavior functions for the robot
    driveStraight(distance, speed) {
        return post("robot/behavior/drive_straight", {
            distance: distance,
            speed: speed
        })
    }
}

class Robot {
    /**This is the official robot class. API endpoints were organized the
     same way as the python API for Vector.

     All of the api's return Promises
     **/

    constructor() {
        this.behavior = Behavior()
    }

    // Robot functions
    getBatteryState() {
        return get("robot/get_battery_state")
    }


}

let robot = new Robot();
export default robot