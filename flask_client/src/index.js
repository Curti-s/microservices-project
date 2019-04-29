import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

import './index.css';
import * as serviceWorker from './serviceWorker';
import UsersList from './components/UsersList';

class App extends Component {
    constructor() {
        super()
        this.state = {
            users: []
        }
    }

    componentDidMount() {
        this.getUsers();
    }

    getUsers() {
        axios.get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
        .then((res) => {this.setState({users: res.data.data.users});})
        .catch((err) => { console.log(err);})
    }

    render () {
        return (
            <div className="container">
                <div className="row">
                    <div className="col-md-8">
                        <br/>
                        <h1>All Users</h1>
                        <hr/><br/>
                        <UsersList users={this.state.users} />
                    </div>
                </div>
            </div>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
