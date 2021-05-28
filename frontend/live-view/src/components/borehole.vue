<template>
  <div class="col-lg-3 sensor">
    <h6 class="px-3 mt-1 mb-1 sensor-heading">Имя меторождения</h6>
    <h6 class="sensor-heading mb-1">Имя скважины</h6>
    <ul class="list-group">
      <li
        class="
          list-group-item list-group-item-dark
          d-flex
          justify-content-between
          flex-wrap
        "
      >
        <b>Давление</b>
        <div>
          <span class="value"
            ><b>{{ pressure_value }}</b></span
          >
          <b>атм.</b>
        </div>
      </li>
      <li
        class="
          list-group-item list-group-item-dark
          d-flex
          justify-content-between
          flex-wrap
        "
      >
        <b>Тепература</b>
        <div>
          <span class="value"
            ><b>{{ temperature_value }}</b></span
          >
          <b>&#8451;</b>
        </div>
      </li>
      <li
        class="
          list-group-item list-group-item-dark
          d-flex
          justify-content-between
          flex-wrap
        "
      >
        <b>Уровень</b>
        <div>
          <span class="value"
            ><b>{{ waterline_value }}</b></span
          >
          <b>М</b>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "BoreHole",
  props: {
    pressure_value: Number,
    temperature_value: Number,
    waterline_value: Number,
  },
};
</script>
