<template>
  <div ref="chartContainer" style="width: 100%; height: 500px;"></div>
</template>

<script>
import * as echarts from "echarts";

export default {
  name: "StackedBarChart",
  mounted() {
    this.initChart();
  },
  methods: {
    initChart() {
      const chartDom = this.$refs.chartContainer;
      const myChart = echarts.init(chartDom);

      const option = {
        title: {
          text: "Incidents by Weapon and Victim Sex",
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
          bottom: "80%",
          left: "center",
          orient: "horizontal",
        },
        grid: {
          left: "3%",
          right: "4%",
          bottom: "3%",
          containLabel: true,
        },
        xAxis: {
          type: "value",
          name: "Incident Count",
        },
        yAxis: {
          type: "category",
          data: [
            "Strong-Arm (Hands, Fist, Feet or Bodily Force)",
            "Unknown Weapon/Other Weapon",
            "Hand Gun",
            "Verbal Threat",
            "Unknown Firearm",
            "Blade, Cutting Instrument",
            "Knife",
            "Other Known Weapon",
            "Blunt Instrument (Club, Hammer, etc.)",
            "Hand Tool",
            "Improvised Weapon (Rock, Bottle, etc.)",
            "Shotgun",
            "Vehicle",
            "Firearm (Rifle)",
            "Explosives",
            "Ax or Other Sharp Tool",
            "Pepper Spray",
            "Chemical Agent",
            "Fire",
            "Unknown Type of Gun",
          ],
        },
        series: [
          {
            name: "Female (F)",
            type: "bar",
            stack: "Total",
            data: [
              8146, 1896, 1577, 769, 687, 656, 562, 570, 390, 305, 272, 245, 239, 175, 151, 123, 106, 98, 86, 65,
            ],
          },
          {
            name: "Male (M)",
            type: "bar",
            stack: "Total",
            data: [
              2148, 453, 0, 206, 153, 162, 133, 123, 95, 78, 58, 55, 51, 40, 32, 29, 21, 19, 17, 11,
            ],
          },
          {
            name: "Unknown (X)",
            type: "bar",
            stack: "Total",
            data: [
              24121, 4774, 5146, 1705, 1707, 1515, 1213, 1044, 738, 592, 527, 402, 408, 298, 296, 256, 222, 181, 148, 118,
            ],
          },
        ],
      };

      myChart.setOption(option);
    },
  },
};
</script>

<style scoped>
/* Add any necessary styling here */
</style>