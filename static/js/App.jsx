import React from "react";
import Grid from '@material-ui/core/Grid';
import CssBaseline from "@material-ui/core/CssBaseline";
import Card from "@material-ui/core/Card";
import Divider from '@material-ui/core/Divider';
import PropTypes from 'prop-types';

import VectorCameraStream from "./components/VectorCameraStream"
import VectorBatteryStatus from "./components/VectorBatteryStatus"
import VectorMove from "./components/VectorMove"
import ActionPanel from './components/VectorActionPanel'
import {withStyles} from "@material-ui/core";

const styles = theme => ({
    root: {}
});

// Main Page
class App extends React.Component {
    render() {
        return (
            <div>
                <CssBaseline/>

                <Card
                    style={{
                        maxWidth: 1000,
                        marginLeft: "auto",
                        marginRight: "auto"
                    }}>

                    <VectorBatteryStatus/>
                    <Divider/>
                    <Grid container spacing={10}>
                        <Grid item xs={6}>
                            <VectorMove/>
                        </Grid>
                        <Grid item xs={6}>
                            <ActionPanel/>
                        </Grid>
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
