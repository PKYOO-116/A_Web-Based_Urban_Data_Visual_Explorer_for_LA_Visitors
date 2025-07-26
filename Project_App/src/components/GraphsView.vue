<template>
  <div class="visualization-container">
    <div class="charts-wrapper">
      <div class="chart-container">
        <BarChart />
      </div>
      <div class="chart-container">
        <LineChart />
      </div>
    </div>
  </div>
</template>

<script>
import BarChart from './BarChart.vue';
import LineChart from './LineChart.vue';

export default {
  name: 'GraphsView',
  components: {
    BarChart,
    LineChart,
  },
};
</script>

<style scoped>
.visualization-container {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background-color: #f9f9f9;
}

.charts-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: space-evenly;
  align-items: center;
  padding: 20px;
}

.chart-container {
  width: 90%;
  max-width: 1200px;
  height: 45%;  /* slightly less than half to account for spacing */
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  padding: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>