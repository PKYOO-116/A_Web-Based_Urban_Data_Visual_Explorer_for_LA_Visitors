<template>
  <div ref="chartContainer" style="width: 100%; height: 500px;"></div>
</template>

<script>
import * as echarts from "echarts";

export default {
  name: "NightingaleChart",
  mounted() {
    this.initChart();
  },
  methods: {
    initChart() {
      const chartDom = this.$refs.chartContainer;
      const myChart = echarts.init(chartDom);

      // Data for top 40 crime types
      const crimeTypesData = [
        { name: "ASSAULT WITH DEADLY WEAPON, AGGRAVATED ASSAULT", value: 19473 },
        { name: "BATTERY - SIMPLE ASSAULT", value: 14640 },
        { name: "ROBBERY", value: 12059 },
        { name: "INTIMATE PARTNER - SIMPLE ASSAULT", value: 5922 },
        { name: "BRANDISH WEAPON", value: 3376 },
        { name: "INTIMATE PARTNER - AGGRAVATED ASSAULT", value: 2850 },
        { name: "SHOOTING INTO OCCUPIED DWELLING", value: 2487 },
        { name: "CRIMINAL THREATS - NO WEAPON DISPLAYED", value: 2461 },
        { name: "VANDALISM - FELONY ($400 & OVER, ALL CHURCH VANDALISMS)", value: 2343 },
        { name: "BURGLARY FROM VEHICLE", value: 2164 },
        { name: "BURGLARY", value: 2092 },
        { name: "VEHICLE - STOLEN", value: 1876 },
        { name: "BOMB SCARE", value: 1749 },
        { name: "VIOLATION OF RESTRAINING ORDER", value: 1657 },
        { name: "CHILD ABUSE (PHYSICAL)", value: 1349 },
        { name: "OTHER MISCELLANEOUS CRIME", value: 1289 },
        { name: "BATTERY WITH SEXUAL CONTACT", value: 1238 },
        { name: "DRIVING WITHOUT OWNER CONSENT", value: 1126 },
        { name: "THEFT PLAIN - PETTY ($950 & UNDER)", value: 1119 },
        { name: "BOMB THREAT", value: 994 },
        { name: "ARSON", value: 876 },
        { name: "THEFT OF IDENTITY", value: 765 },
        { name: "RAPE, FORCIBLE", value: 718 },
        { name: "SEXUAL BATTERY", value: 662 },
        { name: "EMBEZZLEMENT, GRAND THEFT ($950 & OVER)", value: 621 },
        { name: "VANDALISM - MISDEMEANOR ($399 OR UNDER)", value: 602 },
        { name: "CHILD ANNOYING (SEXUAL)", value: 531 },
        { name: "BRIBERY", value: 418 },
        { name: "STALKING", value: 406 },
        { name: "DRUNK DRIVING VEHICLE", value: 359 },
        { name: "OTHER SEX (NON-FORCIBLE)", value: 341 },
        { name: "FAILURE TO YIELD - POLICE PURSUIT", value: 328 },
        { name: "HUMAN TRAFFICKING - COMMERCIAL SEX ACTS", value: 304 },
        { name: "DOCUMENT WORTHLESS ($200 & UNDER)", value: 291 },
        { name: "OTHER ARSON-RELATED CRIMES", value: 281 },
        { name: "THEFT, AUTO ACCESSORIES", value: 268 },
        { name: "PICKPOCKET", value: 223 },
        { name: "VIOLATION OF COURT ORDER", value: 214 },
        { name: "DISTURBING THE PEACE", value: 206 },
        { name: "RESISTING ARREST", value: 194 },
      ];

      const option = {
        title: {
          text: "Crime Types",
          left: "center",
          textStyle: {
            fontSize: 24, // Make this more prominent
            fontWeight: "bold",
          },
        },
        tooltip: {
          trigger: "item",
        },
        series: [
          {
            name: "Crime Types",
            type: "pie",
            radius: ["30%", "70%"],
            avoidLabelOverlap: false,
            label: {
              show: true,
              position: "outside",
            },
            emphasis: {
              label: {
                show: true,
                fontSize: "32",
                fontWeight: "bold",
              },
            },
            labelLine: {
              show: true,
            },
            data: crimeTypesData.map((item) => ({
              name: item.name,
              value: item.value,
            })),
          },
        ],
      };

      myChart.setOption(option);
    },
  },
};
</script>

<style scoped>
/* Optional styles for better visualization */
</style>