<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  props: ["options"],
  mounted() {
    this.renderChart(
      {
        labels: [
          "January",
          "February",
          "March",
          "April",
          "May",
          "June",
          "July",
        ],
        datasets: [
          {
            label: "Data One",
            backgroundColor: "#737A83",
            data: [40, 39, 10, 40, 39, 80, 40],
          },
        ],
      },
      { responsive: true, maintainAspectRatio: false }
    );
  },
};
</script>

<style></style>
