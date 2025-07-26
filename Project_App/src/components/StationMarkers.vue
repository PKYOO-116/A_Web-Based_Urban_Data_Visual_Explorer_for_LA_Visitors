<template>
  <div class="markers-container"></div>
</template>

<script>
import mapboxgl from 'mapbox-gl';
import * as d3 from 'd3';

export default {
  name: 'StationMarkers',
  props: {
    map: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      markers: [],
      error: null,
      stations: []
    }
  },
  mounted() {
    console.log('StationMarkers mounted');
    this.loadStationData();
  },
  beforeUnmount() {
    console.log('StationMarkers unmounting');
    this.removeAllMarkers();
  },
  methods: {
    async loadStationData() {
      try {
        console.log('Loading bike station data...');
        const response = await fetch('/data/bike_station.csv');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const csvText = await response.text();
        const stationRows = d3.csvParse(csvText);
        
        this.stations = stationRows
          .filter(d => d.Latitude && d.Longitude && d['Kiosk Name'] && d['Kiosk ID'])
          .map(d => ({
            station_id: d['Kiosk ID'],
            name: d['Kiosk Name'],
            latitude: parseFloat(d.Latitude),
            longitude: parseFloat(d.Longitude),
            status: d.Status,
            region: d.Region,
            goLiveDate: d['Go Live Date']
          }));

        console.log(`Loaded ${this.stations.length} bike stations`);
        console.log('Sample station:', this.stations[0]);
        
        this.initializeMarkers();
      } catch (error) {
        console.error('Error loading bike station data:', error);
        this.error = error.message;
      }
    },

    removeAllMarkers() {
      console.log('Removing all markers');
      this.markers.forEach(marker => {
        if (marker) {
          marker.remove();
        }
      });
      this.markers = [];
    },

    initializeMarkers() {
      console.log('Initializing markers');
      if (this.map.loaded()) {
        this.addMarkers();
      } else {
        this.map.on('load', () => {
          this.addMarkers();
        });
      }
    },

    addMarkers() {
      console.log('Adding markers');
      this.removeAllMarkers();

      this.stations.forEach((station, index) => {
        // Create marker element with color based on status
        const markerElement = document.createElement('div');
        const markerColor = station.status === 'Active' ? '#4CAF50' : '#FF5252';
        
        Object.assign(markerElement.style, {
          width: '12px',
          height: '12px',
          backgroundColor: markerColor,
          borderRadius: '50%',
          border: '2px solid white',
          boxShadow: '0 0 5px rgba(0,0,0,0.5)',
          cursor: 'pointer'
        });

        // Create popup with station information
        const popup = new mapboxgl.Popup({
          offset: [0, -10],
          closeButton: true,
          closeOnClick: true
        })
        .setHTML(`
          <div style="padding: 12px;">
            <h3 style="margin: 0 0 8px 0; font-weight: bold;">${station.name}</h3>
            <p style="margin: 0;">Kiosk ID: ${station.station_id}</p>
            <p style="margin: 4px 0;">Status: <span style="color: ${markerColor}; font-weight: bold;">${station.status}</span></p>
            <p style="margin: 4px 0;">Region: ${station.region}</p>
            <p style="margin: 4px 0;">Go Live Date: ${station.goLiveDate}</p>
          </div>
        `);

        // Create and add the marker
        const marker = new mapboxgl.Marker({
          element: markerElement,
          anchor: 'center'
        })
        .setLngLat([station.longitude, station.latitude])
        .setPopup(popup)
        .addTo(this.map);

        this.markers.push(marker);
        console.log(`Added marker ${index + 1} for ${station.name}`);
      });

      console.log(`Total markers added: ${this.markers.length}`);
    }
  }
}
</script>

<style>
.markers-container {
  position: absolute;
  width: 100%;
  height: 100%;
  pointer-events: none;
}

.mapboxgl-popup {
  z-index: 1000;
}

.mapboxgl-popup-content {
  padding: 0;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.2);
  max-width: 300px;
}

.mapboxgl-popup-close-button {
  padding: 4px 8px;
  font-size: 16px;
}
</style>