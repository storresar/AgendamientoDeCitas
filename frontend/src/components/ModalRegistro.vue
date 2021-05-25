<template>
<transition name="modal-fade">
    <div class="modal-backdrop">
        <div class="modal">
        <header class="modal-header">
            <slot name="header">
            AGREGAR USUARIO
            </slot>
            <button
            type="button"
            class="btn-close"
            @click="close"
            >
            x
            </button>
        </header>

        <section class="modal-body">
            <slot name="body">
                <label for="">Usuario:</label>
                <input type="text" v-model.trim="$v.usuario.$model" id="usuario"  autocomplete="off">
                <label for="">Correo:</label>
                <input type="text" v-model.trim="$v.correo.$model" id="usuario"  autocomplete="off">
                <label>Nombre:</label>
                <input type="text" v-model.trim="$v.nombre.$model" id="nombre"  autocomplete="off">
                <label>Apellido:</label>
                <input type="text" v-model.trim="$v.apellido.$model" id="apellido"  autocomplete="off">
                <label>Fecha Nacimiento:</label>
                <input type="date" v-model.trim="$v.fecha.$model" id="fecha">
                <label for="">Contraseña</label>
                <input type="password" v-model.trim="$v.clave.$model" id="">
                <label for="">Confima la contraseña</label>
                <input type="password" v-model.trim="$v.confirma.$model" id="">
                <label for="">Tipo Usuario</label>
                <select v-model="tipo_usuario">
                    <option value="1">PACIENTE</option>
                    <option value="2">FUNCIONARIO</option>
                    <option value="3">ADMINISTRADOR</option>
                </select>
                <div v-if="tipo_usuario == 1" class="if-paciente">
                    <label for="">RH</label>
                    <input type="text" v-model="model" id="">
                    <label for="">Sexo</label>
                    <select v-model="sexo">
                        <option value="M">Masculino</option>
                        <option value="F">Femenino</option>
                    </select>
                    <label for="">Tipo de identificacion</label>
                    <select v-model="tId">
                        <option value="1">Cedula</option>
                        <option value="2">Tarjeta de Identidad</option>
                        <option value="3">Pasaporte</option>
                    </select>
                    <label for="">Identificacion</label>
                    <input type="text" v-model="$v.confirma.$model" id="">
                    
                </div>
            </slot>
        </section>

        <footer class="modal-footer">
            <button id="agregar" @click="agregarUsuario">AGREGAR USUARIO</button>
        </footer>
        </div>
    </div>
    </transition>
</template>

<script>

import { mapActions } from 'vuex'
import { required,minLength, email, sameAs } from 'vuelidate/lib/validators'

export default {
    name: 'Modal',
    data(){
        return{
            nombre: '',
            apellido: '',
            fecha: '',
            usuario: '',
            correo: '',
            clave: '',
            confirma: '',
            tipo_usuario: 2,
            rh: '',
            sexo: 'M',
            tId: 1,
        }
    },
    validations: {
        nombre: {
            required,
            minLength: minLength(2)
        },
        apellido: {
            required,
            minLength: minLength(2)
        },
        fecha: {
            required,
        },
        usuario: {
            required,
            minLength: minLength(8)
        },
        clave: {
            required,
            minLength: minLength(8)
        },
        confirma: {
            sameAsClave: sameAs('clave')
        },
        correo: {
            required,
            email
        },
    },
    methods: {
        ...mapActions(['crearUsuario']),
        submitFormulario(){

        },
        close() {
            this.$emit('close');
        },
        agregarUsuario(){
            console.log()
        }
    },
};
</script>
<style>
.modal-backdrop {
    position: fixed;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    background-color: rgba(0, 0, 0, 0.3);
    display: flex;
    justify-content: center;
    align-items: center;
}

.modal {
    height: 600px;
    width: 500px;
    background: #FFFFFF;
    box-shadow: 2px 2px 20px 1px;
    overflow-x: auto;
    display: flex;
    flex-direction: column;
}

.modal-header,
.modal-footer {
    padding: 25px;
    display: flex;
}

.modal-header {
    position: relative;
    border-bottom: 1px solid #eeeeee;
    color: #4AAE9B;
    justify-content: space-between;
}

.modal-footer {
    border-top: 1px solid #eeeeee;
    flex-direction: column;
    justify-content: flex-end;
}

.modal-body {
    color: black;
    position: relative;
    padding: 30px 10px;
    text-align: left;
    display: grid;
    grid-template-columns: 1;
}
.modal-body input{
    padding: 10px;
    width: 90%;
}
.modal-body select{
        font-family: 'Karla', sans-serif;
        font-size: 15px;
        padding: 10px;
        width: 90%;
}
.btn-close {
    position: absolute;
    top: 0;
    right: 0;
    border: none;
    font-size: 20px;
    padding: 10px;
    cursor: pointer;
    font-weight: bold;
    color: #4AAE9B;
    background: transparent;
}

.btn-green {
    color: white;
    background: #4AAE9B;
    border: 1px solid #4AAE9B;
    border-radius: 2px;
}
#agregar{
    background-color: rgb(20, 149, 158);
    color: white;
    border: none;
    padding: 20px;
    border-radius: 6px;
    font-family: 'Karla', sans-serif;
    font-size: 15px;
}
.modal-fade-enter,
.modal-fade-leave-to {
    opacity: 0;
}

.modal-fade-enter-active,
.modal-fade-leave-active {
    transition: opacity .3s ease;
}
.if-paciente{
    display: grid;
    grid-template-columns: 1;
}
</style>