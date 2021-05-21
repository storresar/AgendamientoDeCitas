<template>
    <section>
        <input type="text" placeholder="Ingrese su usuario" v-model="nombre">
        <input type="password" placeholder="Ingrese su contraseña" v-model="clave">
        <button @click="mandarDatos()">Ingresar</button>
    </section>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    data(){
        return {
           nombre: 'admin',
           clave: 'Santi123' 
        }
    },
    methods:{
        ...mapActions(['aunteticar']),
        mandarDatos(){
            const datos = {usuario:this.nombre, contraseña:this.clave}
            this.aunteticar(datos)
        }
    }
}
</script>
