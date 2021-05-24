<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
import { mapActions } from 'vuex'
export default {
  methods:{
    ...mapActions(['validarToken', 'getUsuario', 'getListaUsuarios'])
  },
  created(){
    if (window.localStorage.getItem('token')){
      this.validarToken(window.localStorage.getItem('token'))
      .then(this.getUsuario(window.localStorage.getItem('usuario')))
      .catch(msg => this.$alert(msg,'Error','warning'))
    }
  }
}
</script>

<style>
    @import url('https://fonts.googleapis.com/css2?family=Karla:ital,wght@1,300&display=swap');
body{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        font-family: 'Karla', sans-serif;
        
    }
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
