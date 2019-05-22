import React from "react";
import { Redirect } from "react-router-dom";

const Form = props => {
  if (props.isAuthenticated) {
    return <Redirect to="/" />;
  }
  return (
    <div>
      <h1>{props.formType}</h1>
      <hr /> <br />
      <form onSubmit={props.handleUserFormSubmit}>
        {props.formType === "Register" && (
          <div className="form-group">
            <input
              name="username"
              className="form-control input-lg"
              type="text"
              placeholder="Username"
              value={props.formData.username}
              onChange={event => props.handleFormChange(event)}
            />
          </div>
        )}
        <div className="form-group">
          <input
            name="email"
            className="form-control input-lg"
            type="email"
            placeholder="example@example.com"
            value={props.formData.email}
            onChange={event => props.handleFormChange(event)}
          />
        </div>
        <div className="form-group">
          <input
            name="password"
            className="form-control input-lg"
            type="password"
            placeholder="Password"
            value={props.formData.password}
            onChange={event => props.handleFormChange(event)}
          />
        </div>
        <input
          type="Submit"
          className="btn btn-outline-dark btn-lg btn-block"
          onChange={event => props.handleFormChange(event)}
          value="Submit"
        />
      </form>
    </div>
  );
};

export default Form;
