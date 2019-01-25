import React from "react";
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import {withStyles} from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import {
    TiArrowBack,
    TiArrowDownThick,
    TiArrowForward,
    TiArrowUpThick,
} from 'react-icons/ti'

import {FaBinoculars, FaCube, FaHome} from 'react-icons/fa'
import robot from '../services/api'


const styles = theme => ({
    root: {
        flexGrow: 1,
        textAlign: 'center'
    },
    button: {
        margin: theme.spacing.unit
    },
    icon: {
        fontSize: "60px"
    }
});

class VectorMove extends React.Component {
    constructor() {
        super();
        this.state = {
            success_straight: false,
            success_turn: false
        };
        this.timer = null;
    };

    driveStraight(distance, speed) {
        robot.behavior.driveStraight(distance, speed)
            .then(
                (result) => {
                    this.setState({
                        success_straight: true
                    });
                },
                (error) => {
                    this.setState({
                        error//
                    });
                }
            )
    };

    turnInPlace(angle, speed, accel) {
        robot.behavior.turnInPlace(angle, speed, accel)
            .then(
                (result) => {
                    this.setState({
                        success_turn: true
                    });
                },
                (error) => {
                    this.setState({
                        error//
                    });
                }
            )
    }

    render() {
        const {success_turn} = this.state;
        const {classes} = this.props;

        let turn_unit = 0.523599; // 30 degrees radians
        let turn_speed = 1.5708;  // 90 degrees / second
        let straight_unit = 100; // mm
        let straight_speed = 60;  // mm/s

        return (
            <div className={classes.root}>
                <Grid container spacing={10}>
                    <Grid item xs={8}>
                        <Button
                            onMouseDown={() => this.driveStraight(
                                straight_unit,
                                straight_speed)}
                            classes={classes.button}
                        >
                            <TiArrowUpThick
                                className={classes.icon}
                            />
                        </Button>
                    </Grid>
                    <Grid item xs={2}>
                        <Button onClick={robot.behavior.driveOnCharger}>
                            <FaHome className={classes.icon}/>
                        </Button>
                    </Grid>
                    <Grid item xs={4}>
                        <Button
                            onMouseDown={() => this.turnInPlace(
                                turn_unit,
                                turn_speed, 0)}
                            classes={classes.button}
                        >
                            <TiArrowBack
                                className={classes.icon}
                            />
                        </Button>
                    </Grid>
                    <Grid item xs={4}>
                        <Button
                            onMouseDown={() => this.turnInPlace(
                                -turn_unit,
                                turn_speed, 0)}

                            classes={classes.button}
                        >
                            <TiArrowForward
                                className={classes.icon}
                            />
                        </Button>
                    </Grid>
                    <Grid item xs={2}>
                        <Button onClick={robot.behavior.driveOffCharger}>
                            <FaBinoculars className={classes.icon}/>
                        </Button>
                    </Grid>
                    <Grid item xs={8}>
                        <Button
                            onMouseDown={() => this.driveStraight(
                                -straight_unit,
                                straight_speed)}
                            classes={classes.button}
                        >
                            <TiArrowDownThick
                                className={classes.icon}
                            />
                        </Button>
                    </Grid>
                    <Grid item xs={2}>
                        <Button onClick={robot.behavior.dockWithCube}>
                            <FaCube className={classes.icon}/>
                        </Button>
                    </Grid>
                </Grid>
            </div>
        )

    }
}

VectorMove.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(VectorMove)