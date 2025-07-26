<template>
  <div id="map-container">
    <!-- Sidebar -->
    <div id="sidebar">
      <!-- Bar Chart -->
      <canvas id="cuisineBarChart"></canvas>

      <!-- Top 3 Restaurants Section -->
      <div id="top-restaurants">
        <h3>Top 3 Most Popular Restaurants</h3>
        <ul>
          <li v-for="(restaurant, index) in topRestaurants" :key="index">
            <strong>{{ restaurant.Name }}</strong><br />
            Cuisine: {{ restaurant.Cuisine }}<br />
            Rating: {{ restaurant.Rating }} ({{ restaurant["Review Count"] }} reviews)<br />
            Address: {{ restaurant.Address }}
          </li>
        </ul>
      </div>
    </div>

    <!-- Map -->
    <div id="map"></div>
  </div>
</template>

<script>
import L from "leaflet";
import "leaflet/dist/leaflet.css";
import "leaflet.heat"; // Heatmap plugin
import "leaflet.markercluster"; // Marker cluster plugin
import "leaflet.markercluster/dist/MarkerCluster.css"; // Cluster styling
import "leaflet.markercluster/dist/MarkerCluster.Default.css"; // Default cluster styling
import Chart from "chart.js/auto";

export default {
  name: "RestaurantHeatmap",
  data() {
    return {
      restaurants: [],
      cuisineToFlag: {
        Chinese: "🇨🇳",
        Korean: "🇰🇷",
        Japanese: "🇯🇵",
        Taiwanese: "🇹🇼",
        Indian: "🇮🇳",
        Thai: "🇹🇭",
        Vietnamese: "🇻🇳",
        Filipino: "🇵🇭",
        Argentine: "🇦🇷",
        Brazilian: "🇧🇷",
        French: "🇫🇷",
        British: "🇬🇧",
        American: "🇺🇸",
        Mexican: "🇲🇽",
        Lebanese: "🇱🇧",
        Mediterranean: "🌍",
        Caribbean: "🌴",
        Belgian: "🇧🇪",
        Ukrainian: "🇺🇦",
        Italian: "🇮🇹",
        Russian: "🇷🇺",
        Polish: "🇵🇱",
        Peruvian: "🇵🇪",
        Singaporean: "🇸🇬",
        Fusion: "🌐",
        Spanish: "🇪🇸",
        Moroccan: "🇲🇦",
        Colombian: "🇨🇴",
        Sardinian: "🇮🇹",
        Portuguese: "🇵🇹",
        German: "🇩🇪",
        Salvadoran: "🇸🇻",
        Indonesian: "🇮🇩",
        Australian: "🇦🇺",
        Cambodian: "🇰🇭",
        Greek: "🇬🇷",
        Armenian: "🇦🇲",
        Georgian: "🇬🇪",
        Cafes: "☕",
        default: "🌍",
      },
      map: null,
      markerCluster: null,
      heatLayer: null,
      topRestaurants: [],
    };
  },
  async mounted() {
    try {
      // Load restaurants data first
      const response = await fetch('/data/restaurants_la.json');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      this.restaurants = await response.json();

      // Then initialize the map
      this.map = L.map("map").setView([34.0522, -118.2437], 10);

      // Add OpenStreetMap tile layer
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
      }).addTo(this.map);

      // Initialize marker cluster group
      this.markerCluster = L.markerClusterGroup();
      this.map.addLayer(this.markerCluster);

      // Add heatmap layer
      this.heatLayer = L.heatLayer([], {
        radius: 20,
        blur: 15,
        maxZoom: 17,
      }).addTo(this.map);

      // Load markers and heatmap dynamically based on map bounds
      this.map.on("moveend", this.updateVisibleData);

      // Initial load
      this.updateVisibleData();
      this.createCuisineBarChart();
      this.findTopRestaurants();
    } catch (error) {
      console.error('Error loading restaurant data:', error);
    }
  },
  methods: {
    updateVisibleData() {
      // Clear existing markers and heatmap data
      this.markerCluster.clearLayers();
      this.heatLayer.setLatLngs([]);

      // Get visible bounds
      const bounds = this.map.getBounds();

      // Filter restaurants within visible bounds
      const visibleRestaurants = this.restaurants.filter((restaurant) =>
        bounds.contains([restaurant.Latitude, restaurant.Longitude])
      );

      // Prepare heatmap data
      const heatData = visibleRestaurants.map((restaurant) => [
        restaurant.Latitude,
        restaurant.Longitude,
        restaurant.Rating / 5, // Normalize rating to 0–1 scale
      ]);

      // Update heatmap layer
      this.heatLayer.setLatLngs(heatData);

      // Add markers to cluster group
      visibleRestaurants.forEach((restaurant) => {
        const cuisineType = restaurant.Cuisine.split(", ")[0].trim();
        const flagEmoji = this.cuisineToFlag[cuisineType] || "🌍";

        const customIcon = L.divIcon({
          html: `<div style="font-size: 24px;">${flagEmoji}</div>`,
          className: "custom-emoji-icon",
          iconSize: [32, 32],
        });

        const marker = L.marker([restaurant.Latitude, restaurant.Longitude], { icon: customIcon });
        marker.bindPopup(
          `<strong>${restaurant.Name}</strong><br>
          Address: ${restaurant.Address}<br>
          Cuisine: ${restaurant.Cuisine}<br>
          Rating: ${restaurant.Rating} (${restaurant["Review Count"]} reviews)<br>
          Price: ${restaurant["Price Range"]}`
        );

        this.markerCluster.addLayer(marker);
      });

      console.log(`Updated visible data: ${visibleRestaurants.length} restaurants`);
    },
    createCuisineBarChart() {
      const cuisineCounts = {};
      this.restaurants.forEach((restaurant) => {
        const cuisine = restaurant.Cuisine.split(", ")[0].trim();
        cuisineCounts[cuisine] = (cuisineCounts[cuisine] || 0) + 1;
      });

      const sortedCuisines = Object.entries(cuisineCounts)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 5);

      const labels = sortedCuisines.map(([cuisine]) => cuisine);
      const data = sortedCuisines.map(([, count]) => count);

      const ctx = document.getElementById("cuisineBarChart").getContext("2d");
      new Chart(ctx, {
        type: "bar",
        data: {
          labels: labels,
          datasets: [
            {
              label: "Number of Restaurants",
              data: data,
              backgroundColor: "rgba(75, 192, 192, 0.6)",
              borderColor: "rgba(75, 192, 192, 1)",
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              display: true,
            },
          },
          scales: {
            x: {
              title: {
                display: true,
                text: "Cuisine",
              },
            },
            y: {
              title: {
                display: true,
                text: "Number of Restaurants",
              },
              beginAtZero: true,
            },
          },
        },
      });
    },
    findTopRestaurants() {
      const popularRestaurants = this.restaurants
        .map((r) => ({
          ...r,
          PopularityScore: r.Rating * r["Review Count"],
        }))
        .sort((a, b) => b.PopularityScore - a.PopularityScore)
        .slice(0, 3);

      this.topRestaurants = popularRestaurants;
      console.log("Top 3 Most Popular Restaurants:", this.topRestaurants);
    },
  },
};
</script>

<style>
/* Layout container for map and sidebar */
#map-container {
  display: flex;
  height: 100vh;
  width: 100vw;
}

/* Sidebar container */
#sidebar {
  width: 25%;
  background: #f8f9fa;
  padding: 80px;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  overflow-y: auto;
}

/* Map container */
#map {
  flex-grow: 1;
}

/* Top Restaurants Section */
#top-restaurants {
  margin-top: 20px;
  padding: 10px;
  background-color: #ffffff;
  border: 1px solid #ddd;
  border-radius: 5px;
}

#top-restaurants h3 {
  margin-bottom: 10px;
  font-size: 16px;
  color: #333;
}

#top-restaurants ul {
  list-style: none;
  padding: 0;
}

#top-restaurants li {
  margin-bottom: 10px;
}

#top-restaurants li strong {
  font-size: 14px;
  color: #222;
}

/* Custom emoji marker styling */
.custom-emoji-icon {
  display: flex;
  justify-content: center;
  align-items: center;
  background: white;
  border-radius: 50%;
  border: 1px solid #ccc;
  width: 32px;
  height: 32px;
  font-size: 24px;
  line-height: 1;
}
</style>
