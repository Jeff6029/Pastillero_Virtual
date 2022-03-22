import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/medicines',
    name: 'MedicinesListPage',
    component: () => import('@/pages/medicines-list/MedicinesListPage.vue'),
  },
  {
    path: '/medicines/:id',
    name: 'MedicineDetailPage',
    component: () => import('@/pages/medicine-detail/MedicineDetailPage.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
