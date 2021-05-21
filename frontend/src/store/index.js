import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router/index.js';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    usuario: '',
    token: '',
  },
  mutations: {
    storeToken(state, pToken){
      state.token = pToken
    },
    setUsuario(state, usuario){
      state.usuario = usuario
    }
  },
  actions: {
    async getUsuario(context, datos){
      const req = await fetch(`http://127.0.0.1:8000/api/usuarios/${datos.usuario}`)
      console.log(req)
      if (req.status === 200){
        const datosUsuario = await req.json()
        context.commit('setUsuario', datosUsuario)
        if (datosUsuario.rol === 3){
          router.push({name: 'Admin'})
        }
      }
    },
    async aunteticar(context, datos){
      const req = await fetch('http://127.0.0.1:8000/api/token/', {
        method : 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          username: datos.usuario,
          password: datos.contraseña
        })
      })
      if (req.status === 200){
        const token = await req.json()
        context.commit('storeToken', token)
        await context.dispatch('getUsuario', datos)
      }
      if (req.status === 401){
        alert("Usuario invalido")
      }
    }
  },
})
