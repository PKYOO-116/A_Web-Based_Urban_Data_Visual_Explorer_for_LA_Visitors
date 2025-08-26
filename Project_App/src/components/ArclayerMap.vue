<template>
  <div id="deck-container" style="width: 100%; height: 100vh;"></div>
</template>

<script>
import { Deck } from "@deck.gl/core";
import { ArcLayer } from "@deck.gl/layers";
import mapboxgl from "mapbox-gl";

export default {
  name: "BikeShareMap",
  data() {
    return {
      mapboxAccessToken: "####", // Change Access token to your own
      mapboxStyle: "mapbox://styles/mapbox/dark-v10", // Mapbox style
      initialViewState: {
        longitude: -118.2437,
        latitude: 34.0522,
        zoom: 10,
        pitch: 40,
        bearing: 0,
      },
      tripData: [],
    };
  },
  mounted() {
    this.initializeMap();
  },
  methods: {
    initializeMap() {
      mapboxgl.accessToken = this.mapboxAccessToken;
      const map = new mapboxgl.Map({
        container: "deck-container",
        style: this.mapboxStyle,
        center: [
          this.initialViewState.longitude,
          this.initialViewState.latitude,
        ],
        zoom: this.initialViewState.zoom,
        pitch: this.initialViewState.pitch,
        bearing: this.initialViewState.bearing,
      });

      fetch("data/metro_trips.csv")
        .then((response) => response.text())
        .then((csvText) => {
          this.tripData = this.parseCSV(csvText);
          
          const arcLayer = new ArcLayer({
            id: 'arc-layer',
            data: this.tripData,
            pickable: true,
            getSourcePosition: d => [d.start_longitude, d.start_latitude],
            getTargetPosition: d => [d.end_longitude, d.end_latitude],
            getSourceColor: [255, 0, 0],
            getTargetColor: [0, 255, 0],
            getWidth: 2,
          });

          new Deck({
            initialViewState: this.initialViewState,
            controller: true,
            layers: [arcLayer],
            onViewStateChange: ({ viewState }) => {
              map.jumpTo({
                center: [viewState.longitude, viewState.latitude],
                zoom: viewState.zoom,
                bearing: viewState.bearing,
                pitch: viewState.pitch,
              });
            },
          });
        })
        .catch((error) => console.error("Failed to load CSV:", error));
    },

    parseCSV(csvText) {
      const lines = csvText.split('\n');
      const headers = lines[0].split(',');
      return lines.slice(1).map(line => {
        const values = line.split(',');
        const row = {};
        headers.forEach((header, index) => {
          row[header.trim()] = values[index];
        });
        return row;
      });
    },
  },
};
</script>

<style>
#deck-container {
  width: 100%;
  height: 100%;
}
</style>
