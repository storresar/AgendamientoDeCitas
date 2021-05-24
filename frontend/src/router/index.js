import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const paginasPublicas = ['/','/login','/registro']

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue')
  },
  {
    path: '/admin',
    name: 'Admin',
    component: () => import('../views/PaginaAdmin.vue')
  },
  {
    path: '/registro',
    name: 'Registro',
    component: () => import('../views/PaginaRegistro.vue')
  }

]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  const requiereAutorizacion = !paginasPublicas.includes(to.path)
  const estaloggeado = window.localStorage.getItem('token')
  if (requiereAutorizacion && !estaloggeado){
    next('/')
  } else if (estaloggeado && !requiereAutorizacion){
    next('/admin')
  } else {
    next()
  }
})

export default router
