import { createRouter, createWebHistory } from 'vue-router'
import DashboardView from '../views/DashboardView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'dashboard',
      component: DashboardView,
    },
    {
      path: '/documents',
      name: 'documents',
      component: () => import('../views/DashboardView.vue'),
    },
    {
      path: '/solar-activities',
      name: 'solar-activities',
      component: () => import('../views/DashboardView.vue'),
    },
    {
      path: '/guided-planning',
      name: 'guided-planning',
      component: () => import('../views/DashboardView.vue'),
    },
    {
      path: '/solar-projects',
      name: 'solar-projects',
      component: () => import('../views/DashboardView.vue'),
    },
    {
      path: '/tax-calculators',
      name: 'tax-calculators',
      component: () => import('../views/DashboardView.vue'),
    },
    {
      path: '/settings',
      name: 'settings',
      component: () => import('../views/DashboardView.vue'),
    },
    {
      path: '/support',
      name: 'support',
      component: () => import('../views/DashboardView.vue'),
    },
  ],
})

export default router
