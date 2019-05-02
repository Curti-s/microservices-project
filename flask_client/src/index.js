import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';

import './index.css';
import * as serviceWorker from './serviceWorker';
import UsersList from './components/UsersList';
import AddUser from './components/AddUser';



class App extends Component {
    constructor() {
        super()
        this.state = {
            users: [],
            username: '',
            email: ''
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

    addUser(event) {
        event.preventDefault();
        const data = {
            username: this.state.username,
            email: this.state.email
        }
        axios.post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
        .then((res) => { 
            this.getUsers();
            this.setState({username: '', email: ''}) 
        })
        .catch((err) => { console.log(err); })
    }

    handleChange(event) {
        const obj = {};
        obj[event.target.name] = event.target.value;
        this.setState(obj);
    }

    render () {
        return (
            <div className="container">
                <div className="row">
                    <div className="offset-md-2 col-md-8">
                        <br/>
                        <h1>All Users</h1>
                        <hr/><br/>
                        <AddUser
                            username={this.state.username}
                            email={this.state.email} 
                            addUser={this.addUser.bind(this)}
                            handleChange={this.handleChange.bind(this)}/>
                        <br/>
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