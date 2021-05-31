<template>
  <div id="app" class="row d-flex justify-content-between">
    <div v-for="(item, idx) in borehole_list" v-bind:key="idx" class="col-lg-3">
      <borehole
        :name="item.well_name"
        :deposit_name="item.deposit_name"
        :pressure_value="item.pressure"
        :pressure_timestamp="item.pressure_timestamp"
        :temperature_value="item.temperature"
        :temperature_timestamp="item.temperature_timestamp"
        :waterline_value="item.level"
        :waterline_timestamp="item.level_timestamp"
      ></borehole>
    </div>
  </div>
</template>

<script>
import Borehole from "./components/borehole.vue";

export default {
  name: "App",
  components: {
    Borehole,
  },
  data: function () {
    return {
      pressure_data: 0,
      temperature_data: 0,
      waterline_data: 0,
      borehole_list: [],
    };
  },

  created: function () {
    fetch("http://localhost:8000/current_values")
      .then((resp) => {
        return resp.json();
      })
      .then((data) => {
        this.borehole_list = data;
      });
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
