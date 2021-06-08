import Vue from "vue";
import App from "./App.vue";
import router from "./router";
require("./assets/css/main.css");

const moment = require("moment");
require("moment/locale/ru");

Vue.use(require("vue-moment"), {
  moment,
});

Vue.config.productionTip = false;

new Vue({
  router,

  render: function (h) {
    return h(App);
  },
}).$mount("#app");
