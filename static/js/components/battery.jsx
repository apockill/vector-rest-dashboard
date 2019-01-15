import React from "react";

class VectorBatteryStatus extends React.Component {
    constructor() {
        super();
        this.state = {isLoaded: false}
    };

    fetchData() {
        fetch("/api/robot/get_battery_state")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        battery_level: result.battery_level
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

        this.interval = setInterval(() => {
            this.fetchData()
        }, 10000)
    }

    componentWillUnmount() {
        // It's necessary to do this otherwise the interval
        // will be executed even if the component is not present anymore.
        clearInterval(this.interval);
    }

    render() {
        const {error, isLoaded, battery_level} = this.state;
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