<template>
    <div id="line-chart-container">
      <canvas id="line-chart"></canvas>
    </div>
  </template>
  
  <script>
  import { Chart } from 'chart.js/auto';
  
  export default {
    name: 'LineChart',
    data() {
      return {
        chart: null, // Reference to the chart instance
      };
    },
    methods: {
      renderChart() {
        const ctx = document.getElementById('line-chart').getContext('2d');
  
        if (this.chart) {
          this.chart.destroy(); // Destroy the previous chart instance if it exists
        }
  
        // Dates for the X-axis
        const labels = ['Jan 1', 'Jan 2', 'Jan 3', 'Jan 4', 'Jan 5', 'Jan 6', 'Jan 7', 'Jan 8', 'Jan 9', 'Jan 10'];
  
        // Made-up non-linear price data for the 3 hotels
        const hotel1Prices = [300, 350, 320, 400, 370, 390, 420, 410, 380, 450];
        const hotel2Prices = [450, 420, 480, 500, 470, 490, 520, 510, 480, 530];
        const hotel3Prices = [700, 750, 730, 770, 740, 760, 780, 750, 720, 790];
  
        // Render the chart
        this.chart = new Chart(ctx, {
          type: 'line',
          data: {
            labels: labels, // Dates
            datasets: [
              {
                label: 'Hollywood Central Suites',
                data: hotel1Prices,
                borderColor: 'rgba(70, 130, 180, 1)', // Steel Blue
                backgroundColor: 'rgba(70, 130, 180, 0.2)', // Light Steel Blue fill
                fill: true,
              },
              {
                label: 'Urban Hollywood Capitol Records Suite',
                data: hotel2Prices,
                borderColor: 'rgba(100, 149, 237, 1)', // Cornflower Blue
                backgroundColor: 'rgba(100, 149, 237, 0.2)', // Light Cornflower fill
                fill: true,
              },
              {
                label: 'Luxurious Studio in Legendary Hollywood Towers',
                data: hotel3Prices,
                borderColor: 'rgba(135, 206, 250, 1)', // Light Sky Blue
                backgroundColor: 'rgba(135, 206, 250, 0.2)', // Light Sky Blue fill
                fill: true,
              },
            ],
          },
          options: {
            responsive: true,
            maintainAspectRatio: false, // Allow flexibility in dimensions
            plugins: {
              legend: {
                position: 'top',
              },
              title: {
                display: true,
                text: 'Hotel Prices from Jan 1 to Jan 10',
              },
            },
            scales: {
              x: {
                title: {
                  display: true,
                  text: 'Date',
                },
              },
              y: {
                title: {
                  display: true,
                  text: 'Price ($)',
                },
                beginAtZero: false, // Start near the lowest value
              },
            },
          },
        });
      },
    },
    mounted() {
      this.renderChart();
    },
  };
  </script>
  
  <style scoped>
  #line-chart-container {
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