import React from "react";

const Form = props => {
  return (
    <div>
      <h1>{props.formType}</h1>
      <hr /> <br />
      <form onSubmit={event => props.handleUserFormSubmit(event)}>
        {props.formType === "Register" && (
          <div className="form-group">
            <input
              name="username"
              className="form-control input-lg"
              type="text"
              placeholder="Username"
              value={props.formData.username}
              onChange={props.handleFormChange}
            />
          </div>
        )}
        <div clasName="form-group">
          <input
            name="email"
            className="form-control input-lg"
            type="email"
            placeholder="example@example.com"
            value={props.formData.email}
            onChange={props.handleFormChange}
          />
        </div>
        <div className="form-group">
          <input
            name="password"
            className="form-control input-lg"
            type="password"
            placeholder="Password"
            required
            value={props.formData.password}
            onChange={props.handleFormChange}
          />
        </div>
        <input
          type="Submit"
          className="btn btn-primary btn-lg btn-block"
          value="Submit"
        />
      </form>
    </div>
  );
};

export default Form;
