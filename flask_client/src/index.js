import React from "react";
import ReactDOM from "react-dom";
import * as serviceWorker from "./serviceWorker";
import { ConnectedRouter } from "react-router-redux";
import { Provider } from "react-redux";
import { Switch, Route } from "react-router-dom";
import App from "./components/App";
import { store, history } from "./redux/store";
import { getUsers, getUser } from "./redux/actions/action";

if (localStorage.Auth) {
  // update localStorage
  store.dispatch({ type: "SET_USER", user: JSON.parse(localStorage.Auth) });
  let _id = JSON.parse(localStorage.Auth)._id;
  getUser(_id).then(res => {
    store.dispatch({ type: "SET_USER", user: res });
  });
}
ReactDOM.render(
  <Provider store={store}>
    <ConnectedRouter history={history}>
      <Switch>
        <Route path="/" component={App} />
      </Switch>
    </ConnectedRouter>
  </Provider>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
