import Vue from 'vue'
import Vuex from 'vuex'
import router from '../router/index.js';

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    usuario: '',
    listaUsuarios: [],
    listaAuditoria: [],
  },
  mutations: {
    storeToken(state, data){
      window.localStorage.setItem('token', data.token)
      window.localStorage.setItem('usuario', data.username)
    },
    deleteToken(){
      window.localStorage.clear()
    },
    setUsuario(state, usuario){
      state.usuario = usuario
    },
    setListaUsuarios(state, usuarios){
      state.listaUsuarios = usuarios.filter((usuario) => usuario.id != state.usuario.id)
      console.log(state.listaUsuarios)
    },
    agregarUsuario(state, usuario){
      state.listaUsuarios.push(usuario)
    },
    setAuditoria(state,lista){
      state.listaAuditoria = lista
    },
  },
  actions: {
    async getUsuario(context, datos){
      const req = await fetch(`http://127.0.0.1:8000/api/usuarios/${datos}`)
      console.log(req)
      if (req.status === 200){
        const datosUsuario = await req.json()
        context.commit('setUsuario', datosUsuario)
        if (datosUsuario.rol === 3){
          return 'Admin';
        }
      }
    },
    async getListaUsuarios(context){
      const req = await fetch('http://127.0.0.1:8000/api/usuarios/')
      if (req.status === 200){
        const datos = await req.json()
        context.commit('setListaUsuarios', datos)
      }
    },
    async getAuditoria(context){
      const req = await fetch('http://127.0.0.1:8000/api/auditoria/',{
      method : 'GET',
      headers: {
        'Authorization': `Bearer ${window.localStorage.getItem('token')}`
      }
    })
      console.log(req)
      if (req.status === 200){
        const datosAuditoria = await req.json()
        context.commit('setAuditoria', datosAuditoria)
      }
    },
    async autenticar(context, datos){
      const req = await fetch('http://127.0.0.1:8000/api/usuarios/login/', {
        method : 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos)
      })
      if (req.status === 201){
        const data = await req.json()
        context.commit('storeToken', {token:data.token, username:data.usuario.username})
        context.commit('setUsuario', data.usuario)
        router.push({name:'Admin'})
      }
      if (req.status === 401){
        throw 'Error de Autenticación'
      }
    },
    async validarToken(context, token){
      const req = await fetch('http://127.0.0.1:8000/api/token/verify/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          token:token
        })
      })
      if (req.status !== 200){
        context.commit('deleteToken')
        throw  'Session caducada'
      } else {
        await context.dispatch('getUsuario', window.localStorage.getItem('username'))
      }
    },
    async eliminarUsuario(context, nombreUsuario){
      const req = await fetch(`http://127.0.0.1:8000/api/usuarios/${nombreUsuario}`, {
        method : 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        },
      })
      if (req.status === 200){
        await context.dispatch('getListaUsuarios')
        await context.dispatch('getAuditoria')
        return 'Se ha eliminado el usuario correctamente'
      }
      if (req.status === 401){
        throw 'Error de Autenticación'
      }
    },
    async modificarUsuario(context, datos){
      const usuario = datos.usuario
      const req = await fetch(`http://127.0.0.1:8000/api/usuarios/${usuarioNuevo.username}/`,{
        method : 'PUT',
        headers : {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        },
        body: JSON.stringify(usuarioNuevo)
      })
      
      if (req.status === 200){
        const usuario_r = await req.json()
        await context.dispatch('getListaUsuarios')
        if(usuarioNuevo.rol === 1){
          datos.paciente.usuario_p = usuario_r.id
          await context.dispatch('modificarPaciente', usuario_r)
        }
        return 'Se ha modificado el usuario correctamente'
      }
      if (req.status === 401){
        throw 'Error de Ejecución'
      }
    },
    async crearUsuario(context, datos){
      const usuario = datos.usuario
      const req = await fetch('http://127.0.0.1:8000/api/usuarios/', {
        method : 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        },
        body: JSON.stringify(usuario)
      })
      if (req.status === 201){
        const usuario_r = await req.json()
        context.commit('agregarUsuario', usuario_r)
        console.log(usuario_r)
        if (usuario_r.rol === 1){
          datos.paciente.usuario_p = usuario_r.id
          await context.dispatch('crearPaciente', datos.paciente)
          
        }
        return 'Se ha creado el usuario correctamente'
      }
      if (req.status === 401){
        throw 'Error de Ejecución'
      }
    },
    async crearPaciente(context, paciente){
      console.log(paciente)
      const req = await fetch('http://127.0.0.1:8000/api/pacientes/', {
        method : 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        },
        body: JSON.stringify(paciente)
      })
      console.log(req)
    },
    async modificarPaciente(context, pacienteNuevo){
      const req = await fetch(`http://127.0.0.1:8000/api/usuarios/${pacienteNuevo.usuario_p}/`,{
        method : 'PUT',
        headers : {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        },
        body: JSON.stringify(pacienteNuevo)
      })
    }
  }
})
