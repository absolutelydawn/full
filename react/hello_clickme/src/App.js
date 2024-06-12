import React, { Component } from "react"

class App extends Component {
    state = {
        hello: "Hello App.js!!",
    }

    handleChange = (e) => {
        this.setState({ hello: "Bye App.js!!" });
    }

    render() {
        return (
            <div className="App">
                <div>{this.state.hello}</div>
                <button onClick={this.handleChange}>Click Me!!</button>
            </div>
        )
    }

}

export default App;