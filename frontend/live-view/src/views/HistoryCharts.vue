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
            type="date"
            class="form-control"
            aria-describedby="basic-addon1"
            id="start"
          />
        </div>
        <div class="input-group ms-5">
          <span class="input-group-text" id="basic-addon2">Конец</span>
          <input
            type="date"
            class="form-control"
            aria-describedby="basic-addon2"
            id="end"
          />
        </div>
        <select class="form-select ms-5" aria-label="boreholes-select">
          <option selected>Выбрать скважину</option>
          <option value="1">скважина 36</option>
          <option value="2">скважина 38</option>
          <option value="3">скважина 2-ПЭ</option>
        </select>
        <select class="form-select ms-5" aria-label="data-type-select">
          <option selected>Выбрать параметр</option>
          <option value="1">Температура</option>
          <option value="2">Давление</option>
          <option value="3">Уровень</option>
        </select>
        <button type="button" class="btn btn-primary ms-5">Сформировать</button>
      </div>
    </div>
    <div>
      <line-chart></line-chart>
    </div>
  </div>
</template>

<script>
import LineChart from "@/components/linechart.vue";

export default {
  name: "HistoryCharts",
  components: {
    LineChart,
  },
};
</script>
