import Vue from 'vue'
import VueRouter from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import LoginView from '@/views/LoginView.vue'
import HomeView from '@/views/HomeView.vue'
import CheckoutView from '@/views/CheckoutView.vue'
import SuccessView from '@/views/SuccessView.vue'
import ProfileView from '@/views/ProfileView.vue'



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/login',
    name: 'Login',
    component: LoginView,
  },
  {
    path: '/checkout',
    name: 'Checkout',
    component: CheckoutView,
  },
  {
    path: '/checkout/success',
    name: 'Success',
    component: SuccessView,
  },
  {
    path: '/profile',
    name: 'Profile',
    component: ProfileView,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
