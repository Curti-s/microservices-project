import React from "react";
import { Navbar, Nav } from "react-bootstrap";
import { LinkContainer } from "react-router-bootstrap";

const NavigationBar = props => {
  return (
    <Navbar bg="light" variant="light" className="inverse collapseOnSelect">
      <Navbar.Brand>
        <span>{props.title}</span>
      </Navbar.Brand>
      <Navbar.Toggle />

      <Navbar.Collapse>
        <Nav className="mr-auto">
          <LinkContainer to="/">
            <Nav.Item eventKey={1}>Home</Nav.Item>
          </LinkContainer>
          <LinkContainer to="/about">
            <Nav.Item eventKey={2}>About</Nav.Item>
          </LinkContainer>
          <LinkContainer to="/status">
            <Nav.Item eventKey={3}>User Status</Nav.Item>
          </LinkContainer>
        </Nav>
        <Nav clasName="mr-auto">
          <LinkContainer to="/register">
            <Nav.Item eventKey={1}>Register</Nav.Item>
          </LinkContainer>
          <LinkContainer to="/login">
            <Nav.Item eventKey={2}>Login</Nav.Item>
          </LinkContainer>
          <LinkContainer to="/logout">
            <Nav.Item eventKey={3}>Logout</Nav.Item>
          </LinkContainer>
        </Nav>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default NavigationBar;
