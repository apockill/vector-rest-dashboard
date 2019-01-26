import React from "react";
import CssBaseline from "@material-ui/core/CssBaseline";
import Card from "@material-ui/core/Card";
import Divider from '@material-ui/core/Divider';

import VectorCameraStream from "./components/VectorCameraStream"
import VectorBatteryStatus from "./components/VectorBatteryStatus"
import VectorMove from "./components/VectorMove"
import ActionPanel from './components/VectorActionPanel'

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
                    <VectorMove/>
                    <ActionPanel/>
                    <Divider/>
                    <VectorCameraStream/>
                </Card>
            </div>
        )
    }
}

export default App;
