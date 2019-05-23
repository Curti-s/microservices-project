const initialState = {
  articles: [],
  article: {}
};

export default (state = initialState, action) => {
  if (action.type === "LOAD_ARTICLES") {
    return Object.assign({}, state, {
      articles: action.articles
    });
  }
  if (action.type === "VIEW_ARTICLE") {
    return Object.assign({}, state, {
      article: action.article
    });
  }
  if (action.type === "CLAP_ARTICLE") {
    let article = Object.assign({}, state.article);
    article.claps++;
    return { ...state, article: article };
  }
  return state;
};
