<template>
  <div class="d-flex vh-100 vw-100">
    <div class="sidebar bg-dark text-light">
      <div class="sidebar-header bg-secondary p-3">
        <h2 class="h4 mb-0">LA Info Visualization</h2>
      </div>
      <div class="p-3 d-flex flex-column gap-2">
        <button 
          class="btn btn-lg text-start w-100"
          :class="currentView === 'arc' ? 'btn-primary' : 'btn-outline-light'"
          @click="currentView = 'arc'"
        >
          <i class="bi bi-map me-2"></i>
          Trip Routes & Stations
        </button>
        <button 
          class="btn btn-lg text-start w-100"
          :class="currentView === 'heatmap' ? 'btn-primary' : 'btn-outline-light'"
          @click="currentView = 'heatmap'"
        >
          <i class="bi bi-thermometer-high me-2"></i>
          Crime Heatmap
        </button>
        <button 
          class="btn btn-lg text-start w-100"
          :class="currentView === 'charts' ? 'btn-primary' : 'btn-outline-light'"
          @click="currentView = 'charts'"
        >
          <i class="bi bi-bar-chart me-2"></i>
          Crime Charts
        </button>
        <button 
          class="btn btn-lg text-start w-100"
          :class="currentView === 'map' ? 'btn-primary' : 'btn-outline-light'"
          @click="currentView = 'map'"
        >
          <i class="bi bi-geo-alt me-2"></i>
          Hotel Heatmap
        </button>
        <button 
          class="btn btn-lg text-start w-100"
          :class="currentView === 'graphs' ? 'btn-primary' : 'btn-outline-light'"
          @click="currentView = 'graphs'"
        >
          <i class="bi bi-graph-up me-2"></i>
          Hotel Charts
        </button>
        <button 
          class="btn btn-lg text-start w-100"
          :class="currentView === 'restaurants' ? 'btn-primary' : 'btn-outline-light'"
          @click="currentView = 'restaurants'"
        >
          <i class="bi bi-shop me-2"></i>
          Restaurant Map & Charts
        </button>
      </div>
    </div>
    <div class="main-content flex-grow-1">
      <ArcLayer v-if="currentView === 'arc'" />
      <CrimeHeatmap v-if="currentView === 'heatmap'" />
      <ChartsPage v-if="currentView === 'charts'" />
      <MapVisualization v-if="currentView === 'map'" />
      <GraphsView v-if="currentView === 'graphs'" />
      <RestaurantHeatmap v-if="currentView === 'restaurants'" />
    </div>
  </div>
</template>

<script>
import ArcLayer from './components/ArcLayer.vue';
import CrimeHeatmap from './components/CrimeHeatmap.vue';
import ChartsPage from './components/ChartsPage.vue';
import MapVisualization from './components/MapVisualization.vue';
import GraphsView from './components/GraphsView.vue';
import RestaurantHeatmap from './components/RestaurantHeatmap.vue';

export default {
  name: 'App',
  components: {
    ArcLayer,
    CrimeHeatmap,
    ChartsPage,
    MapVisualization,
    GraphsView,
    RestaurantHeatmap
  },
  data() {
    return {
      currentView: 'arc'
    };
  }
};
</script>

<style>
@import url("https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css");

.sidebar {
  width: 280px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
}

.btn-outline-light:hover {
  background-color: rgba(255, 255, 255, 0.1) !important;
  color: white !important;
}

.main-content {
  height: 100%;
  position: relative;
  overflow: hidden;
}

/* Ensure map containers fill their space */
.main-content, #arc-map, #visualization-map-container {
  height: 100%;
  width: 100%;
}

/* Global styles */
body {
  margin: 0;
  overflow: hidden;
}

* {
  box-sizing: border-box;
}
</style>
