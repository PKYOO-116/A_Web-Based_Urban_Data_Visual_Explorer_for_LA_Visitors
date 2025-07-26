<template>
  <div id="map-container">
    <div id="deck-container"></div>
  </div>
</template>

<script>
import { Deck } from "@deck.gl/core";
import { HexagonLayer } from "@deck.gl/aggregation-layers";
import { MapboxOverlay } from "@deck.gl/mapbox";
import mapboxgl from "mapbox-gl";

export default {
  name: "CrimeHeatmap",
  data() {
    return {
      mapboxAccessToken:
        "pk.eyJ1IjoicGt5b28iLCJhIjoiY20zeXFuamg2MXJiMDJqcTIwcmFmaGZwcCJ9.38iaSAmiK7Hv_Oc-i1741w",
      mapboxStyle: "mapbox://styles/mapbox/dark-v10",
    };
  },
  mounted() {
    this.initializeMap();
  },
  methods: {
    initializeMap() {
      const map = new mapboxgl.Map({
        container: "deck-container",
        style: this.mapboxStyle,
        center: [-118.2437, 34.0522],
        zoom: 10,
        pitch: 40,
        bearing: 0,
        accessToken: this.mapboxAccessToken,
      });

      fetch("data/Preprocessed_Crime_Data.csv")
        .then((response) => response.text())
        .then((csvText) => {
          const rows = csvText.split("\n").map((row) => row.split(","));
          const data = rows.slice(1).map((row) => ({
            lng: parseFloat(row[0]),
            lat: parseFloat(row[1]),
          }));

          const hexagonLayer = new HexagonLayer({
            id: "hexagon-layer",
            data: data,
            getPosition: (d) => [d.lng, d.lat],
            elevationScale: 50,
            radius: 200,
            extruded: true,
            opacity: 0.6,
            colorRange: [
              [255, 255, 178],
              [254, 217, 118],
              [254, 178, 76],
              [253, 141, 60],
              [240, 59, 32],
              [189, 0, 38],
            ],
          });

          const overlay = new MapboxOverlay({
            layers: [hexagonLayer],
          });

          map.addControl(overlay);
        })
        .catch((error) => {
          console.error("Error loading CSV data", error);
        });
    },
  },
};
</script>

<style>
#map-container {
  height: 100vh;
  width: 100vw;
  float: left;
}

#deck-container {
  height: 100%;
  width: 100%;
}
</style>