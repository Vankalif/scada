import Vue from "vue";
import App from "./App.vue";
require("./assets/css/main.css");

const moment = require("moment");
require("moment/locale/ru");

Vue.use(require("vue-moment"), {
  moment,
});

Vue.config.productionTip = false;

new Vue({
  render: function (h) {
    return h(App);
  },
}).$mount("#app");
