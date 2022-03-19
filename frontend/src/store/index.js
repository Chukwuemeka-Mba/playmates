import { createStore } from "vuex";
// import axios from "axios";
export default createStore({
  state: {
    favorites: {
      items: [],
    },
    isAuthenticated: false,
    token: "",
  },
  getters: {},
  mutations: {
    initializeStore(state) {
      if (localStorage.getItem("favorites")) {
        state.favorites = JSON.parse(localStorage.getItem("favorites"));
      } else {
        localStorage.setItem("favorites", JSON.stringify(state.cart));
      }
      if (localStorage.getItem("token")) {
        state.token = localStorage.getItem("token");
        state.isAuthenticated = true;
      } else {
        state.token = "";
        state.isAuthenticated = false;
      }
    },
    addToFavorites(state, item) {
      const exists = state.favorites.items.filter(
        (i) => i.favorites.id === item.favorites.id
      );
      if (exists.length) {
        exists[0].quantity = parseInt(
          exists[0].quantity + parseInt(item.quantity)
        );
      } else {
        state.favorites.items.push(item);
      }
      localStorage.setItem("favorites", JSON.stringify(state.favorites));
    },
    setToken(state, token) {
      state.token = token;
      state.isAuthenticated = true;
    },
    removeToken(state) {
      state.token = "";
      state.isAuthenticated = false;
    },
  },
  actions: {},
  modules: {},
});
