<template>
  <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
    <div class="d-flex align-items-center pt-5 pb-2 mb-3 border-bottom">
      <h1>Серверная</h1>
      <small class="px-3">(сводка за 24ч.)</small>
    </div>
    <div class="d-flex justify-content-between mb-5">
      <div class="t-curr p-2 shadow">Текущая температура {{ t_curr }}</div>
      <div class="t-max p-2 shadow">Максимальная температура {{ t_max }}</div>
      <div class="t-av p-2 shadow">Средняя температура {{ t_avg }}</div>
      <div class="t-min p-2 shadow">Минимальная температура {{ t_min }}</div>
    </div>
    <div>
      <line-chart
        ref="ServerRoomChart"
        :chartData="chartData"
        :options="options"
      ></line-chart>
    </div>
  </div>
</template>

<script>
import LineChart from "@/components/linechart.vue";
import moment from "moment";

const chrtFontColor = "rgb(48, 76, 113)";
const s_date = moment().subtract(1, "days").format("YYYY-MM-DD HH:mm:ss");
const e_date = moment().format("YYYY-MM-DD HH:mm:ss");

export default {
  name: "ServerRoom",
  components: {
    LineChart,
  },

  data() {
    return {
      s_date,
      e_date,
      t_curr: 0,
      t_min: 0,
      t_max: 0,
      t_avg: 0,
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
    this.chartData.labels = data.dates;
    this.chartData.datasets[0].data = data.vals;
    this.t_max = Math.max(...data.vals);
    this.t_min = Math.min(...data.vals);
    this.t_curr = data.vals[data.vals.length - 1];
    let sum = data.vals.reduce((a, b) => a + b, 0);
    this.t_avg = (sum / data.vals.length).toFixed(2);
    this.$refs["ServerRoomChart"].renderChart(this.chartData, this.options);
    return NaN;
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
