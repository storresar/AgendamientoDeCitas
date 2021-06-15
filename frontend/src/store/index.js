import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    usuario: '',
    paciente: '',
    listaUsuarios: [],
    listaAuditoria: [],
    listaParametrizacion: [],
    url: 'http://127.0.0.1:8000/api/',
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
    },
    agregarUsuario(state, usuario){
      state.listaUsuarios.push(usuario)
    },
    setPaciente(state, paciente){
      state.paciente = paciente
    },
    setAuditoria(state,lista){
      state.listaAuditoria = lista
    },
    setParametrizacion(state,lista){
      state.listaParametrizacion = lista
    }
  },
  actions: {
    async getUsuario(context, datos){
      const req = await fetch(`${context.state.url}usuarios/${datos}`)
      if (req.status === 200){
        const datosUsuario = await req.json()
        context.commit('setUsuario', datosUsuario)
        if (datosUsuario.rol === 3){
          return 'Admin';
        }
      }
    },
    async getListaUsuarios(context){
      const req = await fetch(`${context.state.url}usuarios/`)
      if (req.status === 200){
        const datos = await req.json()
        context.commit('setListaUsuarios', datos)
      }
    },
    async getAuditoria(context){
      const req = await fetch(`${context.state.url}auditoria/`,{
        method : 'GET',
        headers: {
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        }
      })
      if (req.status === 200){
        const datos = await req.json()
        context.commit('setAuditoria', datos)
      }
    },
    async getPaciente(context, idUsuario){
      const req = await fetch(`${context.state.url}pacientes/${idUsuario}`,{
        method : 'GET',
        headers: {
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        }
      })
      if (req.status === 200){
        const datosPaciente = await req.json()
        context.commit('setPaciente', datosPaciente)
      } else{
        throw 'Error al cargar el paciente'
      }
    },
    async autenticar(context, datos){
      const req = await fetch(`${context.state.url}usuarios/login/`, {
        method : 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(datos),
      })
      const data = await req.json()
      if (req.status === 201){ 
        context.commit('storeToken', {token:data.token, username:data.usuario.username})
        context.commit('setUsuario', data.usuario)
      }
      if (req.status === 401){
        throw data;
      }
    },
    async validarToken(context, token){
      const req = await fetch(`${context.state.url}token/verify/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          token:token
        })
      })
      if (req.status !== 200){
        console.log('Session expired')
        context.commit('deleteToken')
        throw  'Session caducada'
      }
    },
    async eliminarUsuario(context, nombreUsuario){
      const req = await fetch(`${context.state.url}usuarios/${nombreUsuario}`, {
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
      const usuarioM = datos.usuario
      const pacienteM = datos.paciente
      const req = await fetch(`${context.state.url}usuarios/${usuarioM.username}/`,{
        method : 'PUT',
        headers : {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        },
        body: JSON.stringify(usuarioM)
      })
      
      if (req.status === 200){
        await context.dispatch('getListaUsuarios')
        if(usuarioM.rol === 1){
          if(pacienteM.id){
            await context.dispatch('modificarPaciente', pacienteM)
          } else {
            await context.dispatch('crearPaciente', pacienteM)
          }
        }
        return 'Se ha modificado el usuario correctamente'
      }
      if (req.status === 401){
        throw 'Error de Ejecución'
      }
    },
    async crearUsuario(context, datos){
      const usuario = datos.usuario
      const req = await fetch(`${context.state.url}usuarios/`, {
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
        if (usuario_r.rol === 1){
          datos.paciente.usuario_p = usuario_r.id
          await context.dispatch('crearPaciente', datos.paciente)
          
        }
        return 'Se ha creado el usuario correctamente'
      }
      if (req.status === 405){
        const res = await req.json()
        throw res
      }else{
        throw "Fallo en la creación del usuario"
      }
    },
    async crearPaciente(context, paciente){
      await fetch(`${context.state.url}pacientes/`, {
        method : 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        },
        body: JSON.stringify(paciente)
      })
    },
    async modificarPaciente(context, datos){
      const req = await fetch(`${context.state.url}pacientes/${datos.usuario_p}/`,{
        method : 'PUT',
        headers : {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        },
        body: JSON.stringify(datos)
      })
      if (!req.ok){
        throw 'Error en el servidor. Intentalo mas tarde'
      }
    },
    async getParametrizacion(context){
      const req = await fetch(`${context.state.url}parametrizacion/`,{
        method : 'GET',
        headers: {
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        }
      })
      if (req.status === 200){
        const datos = await req.json()
        context.commit('setParametrizacion', datos)
      }
    },
    async eliminarParametrizacion(context,parametro){
      const req = await fetch(`${context.state.url}parametrizacion/${parametro.id}`, {
        method : 'DELETE',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        },
      })
      if (req.status === 204){
        await context.dispatch('getParametrizacion')
        return 'Se ha eliminado correctamente'
      }
      if (req.status === 401){
        throw 'Error de Autenticación'
      }
    },
    async modificarParametrizacion(context, datos){
      const req = await fetch(`${context.state.url}parametrizacion/${datos.id}/`,{
        method : 'PUT',
        headers : {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        },
        body: JSON.stringify(datos)
      })
      if (req.status === 200){
        await context.dispatch('getParametrizacion')
        return 'Se ha modificado el usuario correctamente'
      }
      if (req.status === 401){
        throw 'Error de Ejecución'
      }
    },
    async crearParametrizacion(context,datos){
      const req = await fetch(`${context.state.url}parametrizacion/`, {
        method : 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${window.localStorage.getItem('token')}`
        },
        body: JSON.stringify(datos)
      })
      if (req.status === 201){
        await context.dispatch('getParametrizacion')
        return 'Se ha creado el usuario correctamente'
      }
      if (req.status === 400){
        const res = await req.json()
        throw res
      }

    }
  }
})
