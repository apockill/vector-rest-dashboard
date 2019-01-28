import React from "react";
import Grid from '@material-ui/core/Grid';
import {withStyles} from '@material-ui/core/styles';
import Slider from '@material-ui/lab/Slider';
import PropTypes from 'prop-types';

const styles = theme => ({
    root: {
        flexGrow: 1,
        textAlign: 'center',
        padding: '30px 0px',
        height: 200,
        width: 70
    },
    slider: {
        // This fixes the slider notch position (Idk why it was necessary...)
        width: 0,
        marginLeft: "auto",
        marginRight: "auto",
    },
    sliderLabel: {
        textAlign: "center",

        // For icons
        fontSize: '45px',

        // For images
        height: "45px"
    }
});


class VectorAngleControl extends React.Component {
    constructor(props) {
        // changeRobotState is a function that takes a value between 0 and 100
        // and moves the robot appropriately
        super(props);
        this.state = {
            value: 50
        };
        this.changeRobotState = props.changeRobotState;
        this.updateState = this.updateState.bind(this)
    }

    render() {
        const {classes, children} = this.props;
        const {value} = this.state;

        return (
            <div className={classes.root}>
                <Grid container spacing={10}>
                    <Grid item xs={12}>
                        <Slider
                            classes={{container: classes.slider}}
                            value={value}
                            onChange={this.updateState}
                            onDragEnd={
                                () => this.changeRobotState(value)
                            }
                            vertical
                        />
                    </Grid>
                    <Grid item xs={12}>
                        <div className={classes.sliderLabel}>
                            {children}
                        </div>
                    </Grid>
                </Grid>
            </div>
        )
    }

    updateState(event, value) {
        console.log(event);
        this.setState({value});
    }
}

VectorAngleControl.propTypes = {
    classes: PropTypes.object.isRequired,
    changeRobotState: PropTypes.func.isRequired
};

export default withStyles(styles)(VectorAngleControl)