import Vue from "vue";
import VueRouter from "vue-router";
import WellView from "@/views/WellView.vue";
import HistoryCharts from "@/views/HistoryCharts.vue";
import Meteo from "@/views/Meteo.vue";
import Tambukan from "@/views/Tambukan.vue";
import Reports from "@/views/Reports.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    component: Login,
    meta: {
      layout: "login",
    },
  },
  {
    path: "/register",
    component: Register,
    meta: {
      layout: "login",
    },
  },
  {
    path: "/live",
    component: WellView,
    meta: {
      layout: "main",
    },
  },
  {
    path: "/charts",
    component: HistoryCharts,
    meta: {
      layout: "main",
    },
  },
  {
    path: "/meteo",
    component: Meteo,
    meta: {
      layout: "main",
    },
  },
  {
    path: "/tambukan",
    component: Tambukan,
    meta: {
      layout: "main",
    },
  },
  {
    path: "/reports",
    component: Reports,
    meta: {
      layout: "main",
    },
  },
];

const router = new VueRouter({
  routes,
});

export default router;
