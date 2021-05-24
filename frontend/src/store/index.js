import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router/index.js';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    usuario: '',
    token: '',
    listaUsuarios: [],
  },
  mutations: {
    storeToken(state, pToken){
      state.token = pToken
    },
    setUsuario(state, usuario){
      state.usuario = usuario
    },
    setListaUsuarios(state, usuarios){
      state.listaUsuarios = usuarios.filter((usuario) => usuario.id != state.usuario.id)
      console.log(state.listaUsuarios)
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
    async getListaUsuarios(context){
      const req = await fetch('http://127.0.0.1:8000/api/usuarios/')
      console.log(req)
      if (req.status === 200){
        const datosUsuario = await req.json()
        context.commit('setListaUsuarios', datosUsuario)
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
        throw 'Error de Autenticación'
      }
    },
    async eliminarUsuario(context, nombreUsuario){
      console.log(context.state.token.access)
      const req = await fetch(`http://127.0.0.1:8000/api/usuarios/${nombreUsuario}`, {
        method : 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${context.state.token.access}`
        },
      })
      if (req.status === 200){
        await context.dispatch('getListaUsuarios')
        return 'Se ha eliminado el usuario correctamente'
      }
      if (req.status === 401){
        throw 'Error de Autenticación'
      }
    },
    async modificarUsuario(context, usuarioNuevo){
      console.log(usuarioNuevo)
      console.log(JSON.stringify(usuarioNuevo))
      const req = await fetch(`http://127.0.0.1:8000/api/usuarios/${usuarioNuevo.username}/`,{
        method : 'PUT',
        headers : {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(usuarioNuevo)
      })
      console.log(req)
      if (req.status === 200){
        await context.dispatch('getListaUsuarios')
        return 'Se ha modificado el usuario correctamente'
      }
      if (req.status === 401){
        throw 'Error de Ejecución'
      }
    },
  },
})
