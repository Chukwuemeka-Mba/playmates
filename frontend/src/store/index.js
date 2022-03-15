import { createStore } from "vuex";
import axios from "axios";
export default createStore({
  state: {
    return: {
      playmates: [],
      bodyCount: "",
    },
  },
  getters: {
    getPlayMates() {
      axios.get("playmates-api/playmates/").then((response) => {
        this.playmates = response.data;
      });
    },
  },
  mutations: {},
  actions: {},
  modules: {},
});
