import axios from "axios";
import React, { Component } from "react";
import { Route, Switch } from "react-router-dom";

import "./index.css";
import UsersList from "./components/UsersList";
import AddUser from "./components/AddUser";
import About from "./components/About";
import NavigationBar from "./components/NavigationBar";
import Form from "./components/Form";

class App extends Component {
  constructor() {
    super();
    this.state = {
      users: [],
      username: "",
      email: "",
      title: "Microservices Project",
      formData: {
        username: "",
        email: "",
        password: ""
      }
    };
  }

  componentDidMount() {
    this.getUsers();
  }

  getUsers() {
    axios
      .get(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`)
      .then(res => {
        this.setState({ users: res.data.data.users });
      })
      .catch(err => {
        console.log(err);
      });
  }

  addUser(event) {
    event.preventDefault();
    const data = {
      username: this.state.username,
      email: this.state.email
    };
    axios
      .post(`${process.env.REACT_APP_USERS_SERVICE_URL}/users`, data)
      .then(res => {
        this.getUsers();
        this.setState({ username: "", email: "" });
      })
      .catch(err => {
        console.log(err);
      });
  }

  handleChange(event) {
    const obj = {};
    obj[event.target.name] = event.target.value;
    this.setState(obj);
  }

  render() {
    return (
      <React.Fragment>
        <NavigationBar title={this.state.title} />
        <div className="container">
          <div className="row">
            <div className="offset-md-4 col-md-4">
              <Switch>
                <Route
                  exact
                  path="/"
                  render={() => (
                    <div>
                      <h1>All Users</h1>
                      <hr /> <br />
                      <AddUser
                        username={this.state.username}
                        email={this.state.email}
                        addUser={this.addUser.bind(this)}
                        handleChange={this.handleChange.bind(this)}
                      />
                      <br />
                      <UsersList users={this.state.users} />
                    </div>
                  )}
                />
                <Route path="/about" component={About} />
                <Route
                  exact
                  path="/register"
                  render={() => (
                    <Form
                      formType={"Register"}
                      formData={this.state.formData}
                    />
                  )}
                />
                <Route
                  exact
                  path="/login"
                  render={() => (
                    <Form formType={"Login"} formData={this.state.formData} />
                  )}
                />
              </Switch>
            </div>
          </div>
        </div>
      </React.Fragment>
    );
  }
}

export default App;
