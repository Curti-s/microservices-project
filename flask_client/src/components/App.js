import React from "react";
import { Switch, Route } from "react-router-dom";
import Header from "./Header";
import Feed from "./Feed";
import Profile from "./Profile";
import ArticleView from "./ArticleView";
import Editor from "./Editor";
import SignInWith from "./SignInWith";
import requireAuthentication from "../utils/requireAuth";

class App extends React.Component {
  render() {
    const pathname = window.location.pathname;
    return (
      <div>
        {!pathname.includes("editor") ? <Header /> : ""}
        <SignInWith />
        <Switch>
          <Route exact path="/" component={Feed} />
          <Route path="/profile/:id" component={Profile} />
          <Route path="/articleview/:id" component={ArticleView} />
          <Route path="/editor" component={requireAuthentication(Editor)} />
          <Route path="**" component={Feed} />
        </Switch>
      </div>
    );
  }
}

export default App;
