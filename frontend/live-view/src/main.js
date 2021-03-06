import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import Vuelidate from "vuelidate";
require("./assets/css/main.css");

Vue.use(Vuelidate);

const moment = require("moment");
require("moment/locale/ru");

Vue.use(require("vue-moment"), {
  moment,
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,

  render: function (h) {
    return h(App);
  },
}).$mount("#app");
