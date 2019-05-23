const defaultState = {
  appName: "",
  modalMode: false
};

export default (state = defaultState, action) => {
  if (action.type === "TOGGLE_MODAL") {
    console.log(`Toggling modal ${action.modalMode}`);
    return Object.assign({}, state, { modalMode: action.modalMode });
  }
  return state;
};
