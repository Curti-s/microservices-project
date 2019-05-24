import axios from "axios";

const url =
  process.env.NODE_ENV === "production"
    ? "/api/"
    : "http://localhost:5000/api/";

export function loadArticles() {
  return dispatch => {
    axios
      .get(`${url}articles`)
      .then(res => {
        dispatch({ type: "LOAD_ARTICLES", articles: res.data });
      })
      .catch(err => {
        console.log(err);
      });
  };
}

export async function getUser(_id) {
  try {
    const res = await axios.get(`${url}user/${_id}`);
    return res.data;
  } catch (err) {
    console.log(err);
  }
}

export function getUserProfile(_id) {
  return dispatch => {
    axios
      .get(`${url}user/profile/${_id}`)
      .then(res => {
        dispatch({ type: "SET_PROFILE", profile: res.data });
      })
      .catch(err => {
        console.log(err);
      });
  };
}

export function getArticle(article_id) {
  return dispatch => {
    axios
      .get(`${url}article/${article_id}`)
      .then(res => {
        dispatch({ type: "VIEW_ARTICLE", article: res.data });
      })
      .catch(err => console.log(err));
  };
}

export function clap(article_id) {
  return dispatch => {
    axios
      .post(`${url}article/clap`, { article_id })
      .then(res => {
        dispatch({ type: "CLAP_ARTICLE" });
      })
      .catch(err => console.log(err));
  };
}

export function follow(id, user_id) {
  return dispatch => {
    axios
      .post(`${url}user/follow`, { id, user_id })
      .then(res => {
        dispatch({ type: "FOLLOW_USER", user_id });
      })
      .catch(err => console.log(err));
  };
}

export function signInUser(user_data) {
  return dispatch => {
    axios
      .post(`${url}/user`, user_data)
      .then(res => {
        let user = res.data;
        localStorage.setItem("Auth", JSON.stringify(user));
        dispatch({ type: "SET_USER", user });
      })
      .catch(err => console.log(err));
  };
}

export function toggleClose() {
  return dispatch => {
    dispatch({ type: "TOGGLE_MODAL", modalMode: false });
  };
}
export function toggleOpen() {
  return dispatch => {
    dispatch({ type: "TOGGLE_MODAL", modalMode: true });
  };
}
