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
  {
    path: '/medicinesadd',
    name: 'MedicinesAddPage',
    component: () => import('@/pages/medicines-add/MedicinesAddPage.vue'),
  },
  {
    path: '/medicines-schedule/:date',
    name: 'MedicinesSchedulePage',
    component: () => import('@/pages/medicines-schedule/MedicinesSchedulePage.vue'),
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})

export default router
