<template>
  <div class="sensor">
    <h6 class="px-3 mt-1 mb-1 sensor-heading">{{ deposit_name }}</h6>
    <h6 class="sensor-heading mb-1">{{ name }}</h6>
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
          <span class="mr-5">
            {{ pressure_timestamp | moment("dd, hh:mm") }}
          </span>
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
          <span class="mr-5">
            {{ temperature_timestamp | moment("dd, hh:mm") }}
          </span>
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
          <span class="mr-5">
            {{ waterline_timestamp | moment("dd, hh:mm") }}
          </span>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "BoreHole",
  props: {
    name: String,
    deposit_name: String,
    pressure_value: Number,
    pressure_timestamp: String,
    temperature_value: Number,
    temperature_timestamp: String,
    waterline_value: Number,
    waterline_timestamp: String,
  },
};
</script>
