<template>
  <div class="col-md-9 ms-sm-auto col-lg-10 px-md-4">
    <div class="align-items-center pt-5 pb-2 mb-3 border-bottom">
      <h1>Наблюдение</h1>
    </div>
    <div class="row d-flex justify-content-between">
      <preloader v-if="preloaderIsActive"></preloader>
      <div
        v-for="(item, idx) in borehole_list"
        v-bind:key="idx"
        class="col-lg-3 mb-3"
      >
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
  </div>
</template>

<script>
import Borehole from "@/components/borehole.vue";
import Preloader from "@/components/preloader.vue";

export default {
  name: "WellView",
  components: {
    Borehole,
    Preloader,
  },
  data: function () {
    return {
      borehole_list: [],
      data_poll: Object,
      preloaderIsActive: true,
    };
  },

  created: function () {
    this.data_poll = setInterval(async () => {
      const f = await fetch("http://localhost:8000/current_values");
      const data = await f.json();
      this.preloaderIsActive = false;
      this.borehole_list = data;
    }, 5000);
  },

  beforeDestroy: function () {
    clearInterval(this.data_poll);
  },
};
</script>
