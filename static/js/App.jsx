import React from "react";
import Button from '@material-ui/core/Button';
import CssBaseline from "@material-ui/core/CssBaseline";
import Card from "@material-ui/core/Card";
import VectorCameraStream from "./components/camera.jsx"



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
                    <Button>
                        Link
                    </Button>

                    <VectorCameraStream/>
                </Card>
            </div>
        )
    }
}

export default App;
