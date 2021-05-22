<template>
    <section class="form_registro">
        <h4>Ingresar</h4>
        <input class="control" type="text" placeholder="Ingrese su usuario" v-model="nombre" autocomplete="off">
        <input class="control" type="password"  placeholder="Ingrese su contraseña" v-model="clave" autocomplete="off" id="clave">
        <input type="checkbox" id="cbox2" value="checkbox" v-model="check">
        <button class="boton" @click="mandarDatos()">Ingresar</button>
        <p>¿No tienes cuenta? <a href="#">Registrate aquí</a></p>
    </section>
</template>

<script>
import { mapActions } from 'vuex'
export default {
    data(){
        return {
            nombre: 'admin',
            clave: 'Santi123',
            check: false
        }
    },
    methods:{
        ...mapActions(['aunteticar']),
        mandarDatos(){
            const datos = {usuario:this.nombre, contraseña:this.clave}
            this.aunteticar(datos)
        },
    },
    watch:{
            check: function(antiguo,nuevo){
                var tipo = document.getElementById("clave");
                if(antiguo) {
                    tipo.type = "text";
                }else{
                    tipo.type = "password";
            }
    },
}
}

</script>
<style>
    *{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
        background-image: linear-gradient(to right, #455e81 , #1b304b);
    }
</style>
<style scoped>

.form_registro{
    width: 400px;
    background: white;
    padding: 20px;
    margin: auto;
    margin-top: 100px;
    font-family: 'Poppins', sans-serif;
    color: black;
}
.form_registro h4{
    font-size: 25px;
    margin-bottom: 30px;
    text-align: center;
    background: white;
}
.control{
    font-family: inherit;
    width: 100%;
    border: 0;
    border-bottom: 2px solid gray;
    outline: 0;
    font-size: 1.0rem;
    color: black;
    padding: 7px 0;
    background: transparent;
    transition: border-color 0.2s;
    margin-bottom: 25px;
}
.control:focus{
    font-family: inherit;
    width: 100%;
    border: 0;
    border-bottom: 2px solid #43e9db;
    outline: 0;
    font-size: 1.0rem;
    color: black;
    padding: 7px 0;
    background: transparent;
    transition: border-color 0.2s;
    margin-bottom: 25px;
}

.form_registro p{
    background: white;
    height: 40px;
    text-align: center;
    font-size: 14px;
}
.form_registro a{
    background: white;
    color: black;
    text-decoration: none;
}
.form_registro i{
    background: white;
    font-size: 22px;
}
.form_registro a:hover{
    color: black;
    text-decoration: underline;
}
.form_registro .boton {
    width: 100%;
    background: gray;
    border: none;
    padding: 20px;
    color: white;
    margin: 20px 0;
    font-size: 12px;
    border-radius: 1px;
}


</style>