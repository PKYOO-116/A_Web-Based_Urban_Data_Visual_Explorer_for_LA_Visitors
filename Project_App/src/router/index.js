import { createRouter, createWebHistory } from 'vue-router'
import ArcLayer from '../components/ArcLayer.vue'
import RestaurantHeatmap from '../components/RestaurantHeatmap.vue'

const routes = [
  {
    path: '/',
    redirect: '/arc'
  },
  {
    path: '/arc',
    name: 'arc',
    component: ArcLayer
  },
  {
    path: '/heatmap',
    name: 'heatmap',
    component: RestaurantHeatmap
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

export default router
