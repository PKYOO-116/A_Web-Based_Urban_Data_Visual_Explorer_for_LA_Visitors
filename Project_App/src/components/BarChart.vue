<template>
  <div id="bar-chart-container">
    <canvas id="bar-chart"></canvas>
  </div>
</template>

<script>
import { Chart } from 'chart.js/auto';
import Papa from 'papaparse';

export default {
  name: 'BarChart',
  data() {
    return {
      chart: null, // Reference to the chart instance
    };
  },
  methods: {
    async loadDataAndRenderChart() {
      const csvPath = '/data/la_hotel.csv';
      const response = await fetch(csvPath);
      const csvData = await response.text();

      // Parse CSV using PapaParse
      const parsedData = Papa.parse(csvData, {
        header: true,
        skipEmptyLines: true,
      });

      // Filter for Zip Code 90028
      const hotels = parsedData.data
        .filter((row) => row['Zip code'] === '90028')
        .sort((a, b) => b['Overall score'] - a['Overall score']) // Sort by Overall Score descending
        .slice(0, 3); // Take top 3 hotels

      // Prepare data for the chart
      const labels = hotels.map((hotel) => hotel.name); // Hotel names
      const cleanliness = hotels.map((hotel) => parseFloat(hotel.Cleanliness));
      const comfort = hotels.map((hotel) => parseFloat(hotel.Comfort));
      const facilities = hotels.map((hotel) => parseFloat(hotel.Facilities));
      const staff = hotels.map((hotel) => parseFloat(hotel.Staff));

      // Render the chart
      this.renderChart(labels, cleanliness, comfort, facilities, staff);
    },
    renderChart(labels, cleanliness, comfort, facilities, staff) {
      const ctx = document.getElementById('bar-chart').getContext('2d');

      if (this.chart) {
        this.chart.destroy(); // Destroy the previous chart instance if it exists
      }

      this.chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: labels, // Hotel names
          datasets: [
            {
              label: 'Cleanliness',
              data: cleanliness,
              backgroundColor: 'rgba(70, 130, 180, 0.7)', // Steel Blue
            },
            {
              label: 'Comfort',
              data: comfort,
              backgroundColor: 'rgba(100, 149, 237, 0.7)', // Cornflower Blue
            },
            {
              label: 'Facilities',
              data: facilities,
              backgroundColor: 'rgba(135, 206, 250, 0.7)', // Light Sky Blue
            },
            {
              label: 'Staff',
              data: staff,
              backgroundColor: 'rgba(176, 224, 230, 0.7)', // Powder Blue
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false, // Allow full control of chart size
          plugins: {
            legend: {
              position: 'top',
            },
            title: {
              display: true,
              text: 'Comparison of Top 3 Hotels in Zip Code 90028',
            },
          },
          scales: {
            x: {
              title: {
                display: true,
                text: 'Hotels',
              },
              ticks: {
                maxRotation: 0, // Prevent tilting
                autoSkip: false, // Ensure all labels are shown
              },
            },
            y: {
              title: {
                display: true,
                text: 'Score',
              },
              beginAtZero: true,
            },
          },
        },
      });
    },
  },
  mounted() {
    this.loadDataAndRenderChart();
  },
};
</script>

<style scoped>
#bar-chart-container {
  width: 100%;
  height: 100%;
  position: relative;
  background-color: #f9f9f9;
  border-radius: 8px;
}

canvas {
  width: 100% !important;
  height: 100% !important; /* Make canvas fill container */
}
</style>