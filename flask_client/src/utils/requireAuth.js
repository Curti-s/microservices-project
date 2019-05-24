import React from "react";
import PropTypes from "prop-types";
import { connect } from "react-redux";

export default function(Component) {
  class Authenticate extends React.Component {
    componentDidMount() {
      if (!this.props.isAuth) {
        this.context.router.history.push("/");
      }
    }
    render() {
      return <Component {...this.props} />;
    }
  }

  Authenticate.contextTypes = {
    router: PropTypes.object.isRequired
  };
  const mapStateToProps = state => {
    return {
      isAuth: state.authUser.isAuth
    };
  };
  return connect(mapStateToProps)(Authenticate);
}
