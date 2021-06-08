import Vue from "vue";
import VueRouter from "vue-router";
import WellView from "../views/WellView.vue";
import HistoryCharts from "../views/HistoryCharts.vue";
import Meteo from "../views/Meteo.vue";
import Tambukan from "../views/Tambukan.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: WellView,
  },
  {
    path: "/charts",
    component: HistoryCharts,
  },
  {
    path: "/meteo",
    component: Meteo,
  },
  {
    path: "/tambukan",
    component: Tambukan,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
