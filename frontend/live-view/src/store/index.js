import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    appConfig: {
      appName: "Прометей",
      copyRightsYear: new Date().getFullYear(),
      orgName: 'АО "Кавминкурортресурсы"',
      orgEmail: "it@kavminkr.ru",
      developerName: "Туршиев Николай Манолисович",
      orgAdress: "357600 г. Ессентуки, Пятигорская 133.",
      apiAdress: "172.16.0.91",
    },
    status: "",
    token: localStorage.getItem("token") || "",
    user: {},
  },
  mutations: {},
  actions: {},
  getters: {
    appConfig(state) {
      return state.appConfig;
    },
  },
});
