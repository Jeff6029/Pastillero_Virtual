import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('@/pages/home/HomePage.vue'),
  },
  {
    path: '/medicineslist',
    name: 'MedicinesList',
    component: () => import('@/pages/medicines-list/MedicinesListPage.vue'),
  },
  {
    path: '/infomedicine',
    name: 'InfoMedicine',
    component: () => import('@/pages/info-medicine/InfoMedicinePage.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
