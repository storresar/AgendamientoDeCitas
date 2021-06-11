import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

Vue.use(VueRouter)

const paginasPrivadas = ['/admin']

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
  },
  {
    path: '/cambiar_clave/:token/:nom_usuario',
    name: 'CambiarClave',
    component: () => import('../views/CambiarClave.vue')
  },
  {
    path: '/recuperar_cuenta',
    name: 'RecuperarCuenta',
    component: () => import('../views/RecuperarCuenta.vue')
  },

]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  const requiereAutorizacion = paginasPrivadas.includes(to.path)
  const estaloggeado = window.localStorage.getItem('token')
  if (requiereAutorizacion && !estaloggeado){
    next('/')
  } else if (estaloggeado && !requiereAutorizacion){
    next('/admin')
  }
  next()
})

export default router
