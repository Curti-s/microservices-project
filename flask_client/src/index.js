import React from "react";
import ReactDOM from "react-dom";
import * as serviceWorker from "./serviceWorker";
import { ConnectedRouter } from "react-router-redux";
import { Provider } from "react-redux";
import { Switch, Route } from "react-router-dom";
import App from "./components/App";
import { store, history } from "./redux/store";

ReactDOM.render(
  <Provider store={store}>
    <ConectedRouter history={history}>
      <Switch>
        <Route path="/" component={App} />
      </Switch>
    </ConectedRouter>
  </Provider>,
  document.getElementById("root")
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
