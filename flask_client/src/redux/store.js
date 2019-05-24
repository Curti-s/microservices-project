import { createStore, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import { composeWithDevTools } from "redux-devtools-extension/developmentOnly";
import { createBrowserHistory } from "history";
import { routerMiddleware } from "connected-react-router";
import reducer from "./reducer";

export const history = createBrowserHistory();

export const store = createStore(
  reducer(history), //root reducer with router state
  composeWithDevTools(applyMiddleware(thunk, routerMiddleware(history)))
);
