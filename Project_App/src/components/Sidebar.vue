<template>
  <div class="sidebar">
    <h2>Map Visualizations</h2>
    <div class="navigation-options">
      <router-link 
        to="/arc" 
        class="nav-option"
        active-class="active"
      >
        Metro Trip Routes
      </router-link>
      
      <router-link 
        to="/heatmap" 
        class="nav-option"
        active-class="active"
      >
        Restaurant Heatmap
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Sidebar'
}
</script>

<style scoped>
.sidebar {
  position: fixed;
  top: 0;
  left: 0;
  height: 100vh;
  width: 250px;
  background-color: white;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
}

.navigation-options {
  margin-top: 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.nav-option {
  padding: 12px 16px;
  cursor: pointer;
  border-radius: 4px;
  transition: all 0.3s ease;
  text-decoration: none;
  color: inherit;
}

.nav-option:hover {
  background-color: #f0f0f0;
}

.nav-option.active {
  background-color: #e0e0e0;
  font-weight: bold;
}

h2 {
  margin-bottom: 20px;
}
</style>
