<template>
  <div class="visualization-container">
    <div id="visualization-map-container"></div>
  </div>
</template>

<script>
import 'mapbox-gl/dist/mapbox-gl.css';
import mapboxgl from 'mapbox-gl';

export default {
  name: 'MapVisualization',
  data() {
    return {
      LA_COORDINATES: {
        longitude: -118.2437,
        latitude: 34.0522,
        zoom: 10
      }
    };
  },
  mounted() {
    mapboxgl.accessToken = 'pk.eyJ1IjoiaGh6aHE5OSIsImEiOiJjbTNudGN5emYxZXQ5Mmxvb3U2cHJ5a3F2In0.Uh3rIJqfU0Oy8X_1w4P4sQ';

    const map = new mapboxgl.Map({
      container: 'visualization-map-container',
      style: 'mapbox://styles/mapbox/dark-v10',
      center: [this.LA_COORDINATES.longitude, this.LA_COORDINATES.latitude],
      zoom: this.LA_COORDINATES.zoom,
      pitch: 35,
      bearing: 0
    });

    map.on('load', () => {
      console.log('Map loaded');
      
      // Add error handling for GeoJSON loading
      map.addSource('zip-scores', {
        type: 'geojson',
        data: '/data/zip_scores.geojson',
      }).on('error', (e) => {
        console.error('Error loading GeoJSON:', e);
      });

      // Add a console log to verify data loading
      map.on('sourcedata', (e) => {
        if (e.sourceId === 'zip-scores' && e.isSourceLoaded) {
          console.log('GeoJSON data loaded successfully');
          const features = map.querySourceFeatures('zip-scores');
          console.log('Number of features loaded:', features.length);
        }
      });

      map.addLayer({
        id: 'choropleth-layer',
        type: 'fill',
        source: 'zip-scores',
        paint: {
          'fill-color': [
            'interpolate',
            ['linear'],
            ['get', 'score'],
            0, '#f1eef6',
            300, '#045a8d',
          ],
          'fill-opacity': 0.7,
        },
      });

      // Force a resize after adding layers
      map.resize();
    });

    // Popup handling
    let popup = new mapboxgl.Popup({
      closeButton: false,
      closeOnClick: false,
    });

    map.on('mousemove', 'choropleth-layer', (e) => {
      if (e.features && e.features.length > 0) {
        const feature = e.features[0];
        popup
          .setLngLat(e.lngLat)
          .setHTML(
            `<div>
              <strong>ZIP Code:</strong> ${feature.properties.ZIPCODE || 'Unknown'}<br>
              <strong>Score:</strong> ${feature.properties.score || 'No data'}
            </div>`
          )
          .addTo(map);
      }
    });

    map.on('mouseleave', 'choropleth-layer', () => {
      popup.remove();
    });

    window.addEventListener('resize', () => {
      map.resize();
    });
  }
};
</script>

<style scoped>
.visualization-container {
  width: 100%;
  height: 100%;
  position: relative;
}

#visualization-map-container {
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
}

.mapboxgl-popup {
  max-width: 250px;
  font: 12px/20px 'Helvetica Neue', Arial, Helvetica, sans-serif;
}

.mapboxgl-popup-content {
  text-align: center;
  padding: 10px;
  background-color: rgba(0, 0, 0, 0.8);
  color: white;
  border-radius: 4px;
}
</style>