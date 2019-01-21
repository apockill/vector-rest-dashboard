import React from "react";
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button';
import {withStyles} from '@material-ui/core/styles';
import PropTypes from 'prop-types';
import {
    TiArrowBack,
    TiArrowDown,
    TiArrowForward,
    TiArrowUp
} from 'react-icons/ti'

import robot from '../services/api'


const styles = theme => ({
    root: {
        flexGrow: 1,
        textAlign: 'center'
    },
    button: {
        margin: theme.spacing.unit
    },
    arrow: {
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
            <Paper className={classes.root}>
                <Grid container spacing={10}>
                    <Grid item xs={10}>
                        <Button
                            onClick={() => this.driveStraight(
                                straight_unit,
                                straight_speed)}
                            classes={classes.button}
                        >
                            <TiArrowUp
                                className={classes.arrow}
                            />
                        </Button>
                    </Grid>
                    <Grid item xs={5}>
                        <Button
                            onClick={() => this.turnInPlace(
                                turn_unit,
                                turn_speed, 0)}
                            classes={classes.button}
                        >
                            <TiArrowBack
                                className={classes.arrow}
                            />
                        </Button>
                    </Grid>
                    <Grid item xs={5}>
                        <Button
                            onClick={() => this.turnInPlace(
                                -turn_unit,
                                turn_speed, 0)}
                            classes={classes.button}
                        >
                            <TiArrowForward
                                className={classes.arrow}
                            />
                        </Button>
                    </Grid>
                    <Grid item xs={10}>
                        <Button
                            onClick={() => this.driveStraight(
                                -straight_unit,
                                straight_speed)}
                            classes={classes.button}
                        >
                            <TiArrowDown
                                className={classes.arrow}
                            />
                        </Button>
                    </Grid>
                </Grid>
            </Paper>
        )

    }
}

VectorMove.propTypes = {
    classes: PropTypes.object.isRequired,
};

export default withStyles(styles)(VectorMove)