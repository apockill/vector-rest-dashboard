import React from "react";
import Grid from '@material-ui/core/Grid';
import CssBaseline from "@material-ui/core/CssBaseline";
import Card from "@material-ui/core/Card";
import Divider from '@material-ui/core/Divider';
import PropTypes from 'prop-types';
import {withStyles} from "@material-ui/core";
import {FaCamera} from 'react-icons/fa'

import VectorCameraStream from "./components/VectorCameraStream"
import VectorBatteryStatus from "./components/VectorBatteryStatus"
import VectorMove from "./components/VectorMove"
import VectorActionPanel from './components/VectorActionPanel'
import VectorAngleControl from './components/VectorAngleControl'
import Robot from "./services/api"

const styles = theme => ({
    root: {}
});

// Main Page
class App extends React.Component {
    render() {
        const {classes} = this.props;

        return (
            <div className={classes.root}>

                <CssBaseline/>

                <Card
                    style={{
                        maxWidth: 1000,
                        marginLeft: "auto",
                        marginRight: "auto"
                    }}>

                    <VectorBatteryStatus/>
                    <Divider/>
                    <Grid container spacing={0}>
                        <Grid item xs={1}>
                            <VectorAngleControl
                                changeRobotState={
                                    (value) => Robot.behavior.setHeadAngle(
                                        -0.380 + (value / 100) * 1.168,
                                        20, 20, 0
                                    )}
                            >
                                <FaCamera/>
                            </VectorAngleControl>
                        </Grid>
                        <Grid item xs={1}>
                            <VectorAngleControl
                                changeRobotState={
                                    (value) => Robot.behavior.setLiftHeight(
                                        value / 100, 20, 20, 0
                                    )}
                            >
                                <img src={"/icons/forklift.png"}
                                     style={{
                                         maxWidth: "100%",
                                         maxHeight: "100%"
                                     }}
                                />
                            </VectorAngleControl>
                        </Grid>
                        <Grid item xs={3}>
                            <VectorMove/>
                        </Grid>
                        <Grid item xs={1}>
                            <VectorActionPanel/>
                        </Grid>
                        <Grid item xs={6}/>
                    </Grid>
                    <Divider/>

                    <VectorCameraStream/>

                </Card>
            </div>
        )
    }
}

App.propTypes = {
    classes: PropTypes.object.isRequired
};

export default withStyles(styles)(App)
