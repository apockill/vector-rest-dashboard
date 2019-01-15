import React from "react";

class VectorBatteryStatus extends React.Component {
    constructor() {
        super();
        this.state = {isLoaded: false,
                      is_charging: "hello",
                      battery_volts: null};
        this.timer = null;
    };

    fetchData() {
        fetch("/api/robot/get_battery_state")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        battery_level: result.battery_volts,
                        is_charging: result.is_charging
                    });
                },
                // Note: it's important to handle errors here
                // instead of a catch() block so that we don't swallow
                // exceptions from actual bugs in components.
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error//
                    });
                }
            )

    };

    componentDidMount() {
        // This will be called just once
        this.fetchData();
        this.timer = setInterval(() => this.fetchData(), 1000);
    }

    componentWillUnmount() {
        // It's necessary to do this otherwise the interval
        // will be executed even if the component is not present anymore.
        clearInterval(this.timer);
    }

    render() {
        const {error, isLoaded, battery_level, is_charging} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>
        } else if (!isLoaded) {
            return <div>Loading...</div>
        } else {
            return (
                <div>
                    Battery Level: {battery_level}
                </div>
            )
        }
    }
}

export default VectorBatteryStatus