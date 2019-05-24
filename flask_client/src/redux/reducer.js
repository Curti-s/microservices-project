import { combineReducers } from "redux";
import articles from "./reducers/articles.reducer";
import authUser from "./reducers/authUser.reducer";
import common from "./reducers/common.reducer";
import { connectRouter } from "connected-react-router";

export default history =>
  combineReducers({
    articles,
    authUser,
    common,
    router: connectRouter(history)
  });
