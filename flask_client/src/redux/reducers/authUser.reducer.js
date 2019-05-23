const initialState = {
  user: {},
  isAuth: false,
  profile: {}
};

export default (state = initialState, action) => {
  if (action.type === "SET_USER") {
    return Object.assign({}, state, {
      isAuth: Object.keys(action.user).length > 0 ? true : false,
      user: action.user
    });
  }
  if (action.type === "FOLLOW_USER") {
    return Object.assign({}, state, {
      user: state.user.concat(action.user_id)
    });
  }
  return state;
};
