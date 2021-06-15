import Vue from "vue";
import VueRouter from "vue-router";
import WellView from "../views/WellView.vue";
import HistoryCharts from "../views/HistoryCharts.vue";
import Meteo from "../views/Meteo.vue";
import Tambukan from "../views/Tambukan.vue";
import Reports from "../views/Reports.vue";

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
  {
    path: "/reports",
    component: Reports,
  },
];

const router = new VueRouter({
  routes,
});

export default router;
