<template>
  <div id="app">
    <borehole
      :pressure_value="pressure_data"
      :temperature_value="temperature_data"
      :waterline_value="waterline_data"
    ></borehole>
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
    };
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
