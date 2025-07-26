<template>
  <div class="visualization-container">
    <div id="arc-map"></div>
    <div class="layer-controls">
      <label class="control-item">
        <input 
          type="checkbox" 
          v-model="showMarkers"
        >
        Show Station Markers
      </label>
      <label class="control-item">
        <input 
          type="checkbox" 
          v-model="showArcs"
        >
        Show Trip Routes
      </label>
    </div>
    <StationMarkers 
      v-if="map && showMarkers" 
      :map="map"
      :key="`markers-${showMarkers}`"
    />
    <div v-if="error" class="error-message">
      {{ error }}
    </div>
    <div v-if="tooltip" class="tooltip" :style="tooltipStyle">
      <p><strong>Trip ID:</strong> {{ tooltip.tripId }}</p>
      <p><strong>Duration:</strong> {{ tooltip.duration }} mins</p>
      <p><strong>Start Time:</strong> {{ tooltip.startTime }}</p>
      <p><strong>End Time:</strong> {{ tooltip.endTime }}</p>
    </div>
  </div>
</template>

<script>
import { Deck } from '@deck.gl/core';
import { ArcLayer } from '@deck.gl/layers';
import { MapboxOverlay } from "@deck.gl/mapbox";
import mapboxgl from 'mapbox-gl';
import * as d3 from 'd3';
import 'mapbox-gl/dist/mapbox-gl.css';
import StationMarkers from './StationMarkers.vue';

export default {
  name: 'ArcLayer',
  components: {
    StationMarkers
  },
  data() {
    return {
      tripData: [],
      map: null,
      deck: null,
      tooltip: null,
      error: null,
      showMarkers: true,
      showArcs: true,
      arcLayer: null,
      overlay: null,
      LA_COORDINATES: {
        longitude: -118.2437,
        latitude: 34.0522,
        zoom: 10
      },
      isClicking: false,
    };
  },
  watch: {
    showArcs(newValue) {
      console.log('Arc layer visibility changed:', newValue);
      if (this.map) {
        if (newValue) {
          this.addArcLayer();
        } else {
          this.removeArcLayer();
        }
      }
    }
  },
  computed: {
    tooltipStyle() {
      if (!this.tooltip) return {};
      return {
        left: `${this.tooltip.x}px`,
        top: `${this.tooltip.y}px`,
        display: 'block'
      };
    }
  },
  methods: {
    removeArcLayer() {
      console.log('Removing arc layer');
      if (this.overlay && this.map) {
        this.map.removeControl(this.overlay);
        this.overlay = null;
      }
    },

    addArcLayer() {
      console.log('Adding arc layer');
      if (!this.tripData.length) {
        console.warn('No trip data available');
        return;
      }

      // Remove existing layer if any
      this.removeArcLayer();

      const arcLayer = new ArcLayer({
        id: 'arc-layer',
        data: this.tripData,
        pickable: true,
        autoHighlight: true,
        getSourcePosition: d => d.sourcePosition,
        getTargetPosition: d => d.targetPosition,
        getSourceColor: [255, 165, 0, 255],
        getTargetColor: [0, 255, 255, 255],
        getWidth: 5,
        getHeight: 2,
        getTilt: 60,
        highlightColor: [255, 255, 0, 255],
        parameters: {
          depthTest: false
        },
        pickingRadius: 10,
        onClick: (info) => {
          console.log('Arc clicked:', info);
          // Show tooltip on click
          if (info.object) {
            const x = info.x;
            const y = info.y - 100;
            this.tooltip = {
              x,
              y,
              tripId: info.object.tripId,
              duration: Math.round(info.object.duration),
              startTime: new Date(info.object.startTime).toLocaleTimeString(),
              endTime: new Date(info.object.endTime).toLocaleTimeString()
            };
            console.log('Tooltip data on click:', this.tooltip);
          }
        },
        onHover: (info) => {
          console.log('Arc hover event:', info);
          if (info.object) {
            const x = info.x;
            const y = info.y - 100;
            this.tooltip = {
              x,
              y,
              tripId: info.object.tripId,
              duration: Math.round(info.object.duration),
              startTime: new Date(info.object.startTime).toLocaleTimeString(),
              endTime: new Date(info.object.endTime).toLocaleTimeString()
            };
            console.log('Tooltip data on hover:', this.tooltip);
          } else {
            // Only clear tooltip if we're not clicking
            if (!this.isClicking) {
              this.tooltip = null;
            }
          }
        }
      });

      this.overlay = new MapboxOverlay({
        layers: [arcLayer]
      });

      this.map.addControl(this.overlay);
      
      // Add click handler to map to clear tooltip when clicking outside arcs
      this.map.on('click', (e) => {
        // Check if we clicked on an arc
        const features = this.map.queryRenderedFeatures(e.point, {
          layers: ['arc-layer']
        });
        if (features.length === 0) {
          this.tooltip = null;
        }
      });

      console.log('Arc layer added successfully');
    },

    async loadData() {
      console.log('Loading trip data...');
      try {
        const tripResponse = await fetch('/data/metro_trips.csv');
        if (!tripResponse.ok) {
          throw new Error(`HTTP error! status: ${tripResponse.status}`);
        }
        const tripCsvText = await tripResponse.text();
        
        const tripRows = d3.csvParse(tripCsvText);
        this.tripData = tripRows
          .slice(0, 400)
          .filter(d => {
            return d.start_lon && d.start_lat && d.end_lon && d.end_lat &&
                   d.duration && d.start_time && d.end_time && d.trip_id;
          })
          .map(d => ({
            sourcePosition: [parseFloat(d.start_lon), parseFloat(d.start_lat)],
            targetPosition: [parseFloat(d.end_lon), parseFloat(d.end_lat)],
            duration: parseFloat(d.duration),
            startTime: d.start_time,
            endTime: d.end_time,
            tripId: d.trip_id
          }));

        console.log('Sample trip data:', this.tripData[0]);
        console.log('Processed trips:', this.tripData.length);
      } catch (error) {
        console.error('Error loading trip data:', error);
        this.error = `Error loading data: ${error.message}`;
      }
    },

    initializeMap() {
      console.log('Initializing map...');
      mapboxgl.accessToken = 'pk.eyJ1IjoiY2luZHlqaWFuZzcyMyIsImEiOiJjbTN1ZzFvejIwaXRzMmtwanY2bHhyaGZhIn0.iF1yLwdVECmp-y83zYzYLg';

      this.map = new mapboxgl.Map({
        container: 'arc-map',
        style: 'mapbox://styles/mapbox/dark-v10',
        center: [this.LA_COORDINATES.longitude, this.LA_COORDINATES.latitude],
        zoom: this.LA_COORDINATES.zoom,
        pitch: 35,
        bearing: 0
      });

      this.map.on('load', () => {
        console.log('Map loaded');
        if (this.showArcs) {
          this.addArcLayer();
        }
      });
    }
  },
  async mounted() {
    console.log('ArcLayer mounted');
    try {
      await this.loadData();
      this.initializeMap();
    } catch (error) {
      console.error('Error in ArcLayer:', error);
      this.error = `Error loading data: ${error.message}`;
    }
  },
  beforeUnmount() {
    this.removeArcLayer();
    if (this.map) {
      this.map.remove();
    }
  }
};
</script>

<style scoped>
.visualization-container {
  width: 100%;
  height: 100%;
  position: relative;
}

#arc-map {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.tooltip {
  position: fixed;
  background-color: rgba(0, 0, 0, 0.9);
  color: white;
  padding: 12px 16px;
  border-radius: 6px;
  font-size: 13px;
  pointer-events: none;
  z-index: 10000;
  max-width: 300px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
  transform: translate(-50%, -100%);
  transition: all 0.1s ease;
  border: 1px solid rgba(255, 255, 255, 0.2);
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
}

.tooltip p {
  margin: 4px 0;
  line-height: 1.4;
}

.tooltip strong {
  color: #00ffff;
}

.error-message {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: rgba(255, 0, 0, 0.8);
  color: white;
  padding: 20px;
  border-radius: 4px;
  z-index: 1000;
}

.layer-controls {
  position: absolute;
  top: 20px;
  right: 20px;
  background-color: rgba(255, 255, 255, 0.9);
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.3);
  z-index: 1000;
}

.control-item {
  display: flex;
  align-items: center;
  margin: 8px 0;
  cursor: pointer;
  user-select: none;
}
</style>