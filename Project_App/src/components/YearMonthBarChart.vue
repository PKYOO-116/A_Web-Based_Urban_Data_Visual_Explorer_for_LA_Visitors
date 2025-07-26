<template>
  <div ref="chartContainer" style="width: 100%; height: 600px;"></div>
</template>

<script>
import * as echarts from "echarts";

export default {
  name: "YearMonthBarChart",
  mounted() {
    this.initChart();
  },
  methods: {
    initChart() {
      const chartDom = this.$refs.chartContainer;
      const myChart = echarts.init(chartDom);

      // Data for the chart
      const monthLabels = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
      ];

      const data = {
        2020: [2028, 1972, 1629, 1684, 2101, 2114, 2146, 2418, 2173, 2276, 1919, 1826],
        2021: [814, 797, 885, 896, 929, 922, 1077, 1121, 903, 825, 740, 630],
        2022: [1320, 1316, 1481, 1473, 1587, 1682, 1641, 1600, 1560, 1531, 1282, 1218],
        2023: [1271, 1117, 1288, 1390, 1518, 1477, 1602, 1631, 1592, 1595, 1354, 1324],
        2024: [1264, 1192, 970, 735, 294, 81, 65, 81, 82, 72, 28, 0],
      };

      const years = Object.keys(data);

      const series = years.map((year) => ({
        name: year,
        type: "bar",
        stack: "total",
        data: data[year],
      }));

      const option = {
        title: {
          text: "Incidents by Year and Month",
          left: "center",
          textStyle: {
            fontSize: 24, // Make this more prominent
            fontWeight: "bold",
          },
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
        },
        legend: {
          bottom: 0,
          data: years,
        },
        xAxis: {
          type: "category",
          data: monthLabels,
        },
        yAxis: {
          type: "value",
          name: "Number of Incidents",
        },
        series: series,
      };

      myChart.setOption(option);

      // Resize chart dynamically
      window.addEventListener("resize", myChart.resize);
    },
  },
  beforeUnmount() {
    // Cleanup event listener
    window.removeEventListener("resize", this.myChart?.resize);
  },
};
</script>

<style scoped>
/* Add any additional styles if necessary */
</style>