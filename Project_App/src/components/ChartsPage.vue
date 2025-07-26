<template>
  <div class="charts-container">
    <div class="chart-section">
      <NightingaleChart />
    </div>
    <div class="chart-section">
      <StackedBarChart />
    </div>
    <div class="chart-section">
      <YearMonthBarChart />
    </div>
  </div>
</template>

<script>
import NightingaleChart from "@/components/NightingaleChart.vue";
import StackedBarChart from "@/components/StackedBarChart.vue";
import YearMonthBarChart from "@/components/YearMonthBarChart.vue";

export default {
  name: "ChartsPage",
  components: { NightingaleChart, StackedBarChart, YearMonthBarChart },
};
</script>

<style scoped>
.charts-container {
  display: flex;
  flex-direction: column;
  gap: 40px; /* Add space between charts */
  padding: 20px;
}

.chart-section {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.chart-title {
  font-size: 24px; /* Increase font size for titles */
  font-weight: bold;
  margin-bottom: 20px; /* Add space between title and chart */
}
</style>