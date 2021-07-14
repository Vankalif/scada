<template>
  <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
    <div class="d-flex align-items-center pt-5 pb-2 mb-3 border-bottom">
      <h1>Серверная</h1>
      <small class="px-3">(сводка за 3 дня)</small>
    </div>
    <div class="d-flex justify-content-between mb-5">
      <div class="t-curr p-2">Текущая температура 23.68</div>
      <div class="t-max p-2">Максимальная температура 25.8</div>
      <div class="t-av p-2">Средняя температура 22.68</div>
      <div class="t-min p-2">Минимальная температура 20.1</div>
    </div>
    <div>
      <line-chart
        ref="lineChart"
        :chartData="chartData"
        :options="options"
      ></line-chart>
    </div>
  </div>
</template>

<script>
import LineChart from "@/components/linechart.vue";

var chrtFontColor = "rgb(48, 76, 113)";
const _e_date = new Date();
const offset = _e_date.getDate() - 3;
const _s_year = _e_date.getFullYear();
const _s_month = _e_date.getMonth();
const _s_date = new Date(_s_year, _s_month, offset);
const _builded_s_date = _s_date.toISOString().split("T")[0];
const _builded_e_date = _e_date.toISOString().split("T")[0];

export default {
  name: "ServerRoom",
  components: {
    LineChart,
  },

  data() {
    return {
      s_date: _builded_s_date,
      e_date: _builded_e_date,
      chartData: {
        labels: [
          "Понедельник",
          "Вторник",
          "Среда",
          "Четверг",
          "Пятница",
          "Суббота",
          "Воскресенье",
        ],
        datasets: [
          {
            label: "Температурный график",
            fill: false,
            borderColor: "#304C71",
            data: [40, 39, 10, 40, 39, 80, 40],
          },
        ],
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          labels: { fontColor: chrtFontColor },
        },
        scales: {
          yAxes: [{ ticks: { fontColor: chrtFontColor } }],
          xAxes: [{ ticks: { fontColor: chrtFontColor } }],
        },
      },
    };
  },
  mounted: async function () {
    const resp = await fetch(
      `http://172.16.0.91:8000/get_server_room_sensors_data?sdate=${this.s_date}&edate=${this.e_date}`
    );
    const data = await resp.json();
    console.log(data);
    return data;
  },
};
</script>

<style scoped>
.t-curr {
  background-color: #7fd5ff;
  border-radius: 10px;
}
.t-max {
  background-color: rgb(250, 148, 52);
  border-radius: 10px;
}
.t-av {
  background-color: gold;
  border-radius: 10px;
}
.t-min {
  background-color: #90df17;
  border-radius: 10px;
}
</style>
