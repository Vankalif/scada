<template>
  <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
    <div class="align-items-center pt-3 pb-2 mb-3">
      <div
        class="
          d-flex
          justify-content-between
          flex-wrap flex-md-nowrap
          align-items-center
          pt-3
          pb-2
          mb-3
          border-bottom
        "
      >
        <h1>График</h1>
        <div class="input-group ms-5">
          <span class="input-group-text" id="basic-addon1">Начало</span>
          <input
            v-model="s_date"
            type="date"
            class="form-control"
            aria-describedby="basic-addon1"
            id="start"
          />
        </div>
        <div class="input-group ms-5">
          <span class="input-group-text" id="basic-addon2">Конец</span>
          <input
            v-model="e_date"
            type="date"
            class="form-control"
            aria-describedby="basic-addon2"
            id="end"
          />
        </div>
        <select
          class="form-select ms-5"
          aria-label="boreholes-select"
          v-model="w_id"
        >
          <option selected>Выбрать скважину</option>
          <option value="1">5-0</option>
          <option value="2">5-0-БИС</option>
          <option value="4">5-0-БИС-РЭ</option>
          <option value="3">5-0-РЭ</option>
          <option value="5">1-ПЭ</option>
          <option value="6">89-а</option>
          <option value="7">1-КМВ-БИС</option>
        </select>
        <select
          class="form-select ms-5"
          aria-label="data-type-select"
          v-model="data_table"
        >
          <option selected>Выбрать параметр</option>
          <option value="temperature">Температура</option>
          <option value="pressure">Давление</option>
          <option value="level">Уровень</option>
        </select>
        <button @click="fillData()" type="button" class="btn btn-primary ms-5">
          Сформировать
        </button>
      </div>
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

export default {
  name: "HistoryCharts",
  components: {
    LineChart,
  },

  data() {
    return {
      s_date: undefined,
      e_date: undefined,
      w_id: "Выбрать скважину",
      data_table: "Выбрать параметр",
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
            label: "Пример данных",
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

  methods: {
    fillData: async function () {
      const f = await fetch(
        `http://localhost:8000/get_chart/${this.data_table}?sdate=${this.s_date}&edate=${this.e_date}&w_id=${this.w_id}`
      );
      const data = await f.json();
      this.chartData.datasets[0].label = this.data_table;
      this.chartData.labels = data.dates;
      this.chartData.datasets[0].data = data.vals;
      this.$refs["lineChart"].renderChart(this.chartData, this.options);
    },
  },
};
</script>
