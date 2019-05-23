import { combineReducers } from "react-redux";
import articles from "./reducers/articles.reducer";
import authUser from "./reducers/authUser.reducer";
import common from "./reducers/common.reducer";
import { routerReducer } from "react-router-redux";

export default combineReducers({
  articles,
  authUser,
  common,
  router: routerReducer
});
