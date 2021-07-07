<template>
  <div class="sensor shadow">
    <div class="sensor-heading">
      <h6 class="mt-1 mb-1">{{ deposit_name }}</h6>
      <h6 class="mb-1">{{ name }}</h6>
    </div>
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
            {{ pressure_timestamp | moment("DD/MM, HH:mm") }}
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
            {{ temperature_timestamp | moment("DD/MM, HH:mm") }}
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
            {{ waterline_timestamp | moment("DD/MM, HH:mm") }}
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
    name: {
      type: String,
      default: "N/A",
    },
    deposit_name: {
      type: String,
      default: "N/A",
    },
    pressure_value: {
      type: Number,
      default: 0,
    },
    pressure_timestamp: {
      type: String,
      default: "N/A",
    },
    temperature_value: {
      type: Number,
      default: 0,
    },
    temperature_timestamp: {
      type: String,
      default: "N/A",
    },
    waterline_value: {
      type: Number,
      default: 0,
    },
    waterline_timestamp: {
      type: String,
      default: "N/A",
    },
  },
};
</script>

<style scoped>
.sensor-heading {
  background-color: #626a74;
  text-transform: uppercase;
  padding-left: 1rem;
  text-align: left;
  color: #fff;
}

.value {
  margin-right: 5px;
}
</style>
