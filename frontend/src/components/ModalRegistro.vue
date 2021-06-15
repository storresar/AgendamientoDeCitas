<template>
<transition name="modal-fade">
    <div class="modal-backdrop">
        <div class="modal">
        <header class="modal-header">
            <strong>AGREGAR USUARIO</strong>
            <button
            type="button"
            class="btn-close"
            @click="close"
            >X</button>
        </header>
        <section class="modal-body">
                <label for="">Usuario:</label>
                <input type="text" v-model.trim="$v.nombreUsuario.$model" autocomplete="off">
                <div class="error" v-if="!$v.nombreUsuario.minLength">Este campo requiere minimo 8 caracteres</div>
                <div class="error" v-if="!$v.nombreUsuario.contieneMayuscula">Tiene que escribir todo en minuscula</div>
                <div class="error" v-if="!$v.nombreUsuario.noCaracteresEspeciales">No se admiten caracteres especiales</div>
                <div class="error" v-if="!$v.nombreUsuario.noEspacios">No se admiten espacios</div>
                <label for="">Correo:</label>
                <input type="text" v-model.trim="$v.correo.$model" autocomplete="off">
                <div class="error" v-if="!$v.correo.email">Este correo es invalido</div>
                <label>Nombre:</label>
                <input type="text" v-model.trim="$v.nombre.$model" id="nombre"  autocomplete="off">
                <div class="error" v-if="!$v.nombre.minLength">Este campo requiere minimo 3 caracteres</div>
                <div class="error" v-if="!$v.nombre.noCaracteresEspeciales">No se admiten caracteres especiales ni numeros</div>
                <label>Apellido:</label>
                <input type="text" v-model.trim="$v.apellido.$model" id="apellido"  autocomplete="off">
                <div class="error" v-if="!$v.apellido.minLength">Este campo requiere minimo 8 caracteres</div>
                <div class="error" v-if="!$v.apellido.noCaracteresEspeciales">No se admiten caracteres especiales ni numeros</div>
                <label>Fecha Nacimiento:</label>
                <input type="date" v-model.trim="$v.fecha.$model" id="fecha" min="1905-01-01">
                <div class="error" v-if="!$v.fecha.required">Este campo es obligatorio</div>
                <div class="error" v-if="!$v.fecha.validacionFecha">Esta fecha no es valida</div>
                <label for="">Contraseña</label>
                <input type="password" v-model.trim="$v.clave.$model" id="" maxlength="8" minlength="5">
                <div class="error" v-if="!$v.clave.minLength">Este campo requiere minimo 5 caracteres</div>
                <div class="error" v-if="!$v.clave.esFuerte">La contraseña debe contener una mayuscula, una minuscula y un numero</div>
                <label for="">Confima la contraseña</label>
                <input type="password" v-model.trim="$v.confirma.$model" id="">
                <div class="error" v-if="!$v.confirma.required">Este campo es obligatorio</div>
                <div class="error" v-if="!$v.confirma.sameAsClave">Las claves no coinciden</div>
                <label for="">Tipo Usuario</label>
                <select v-model="tipo_usuario">
                    <option value="1">PACIENTE</option>
                    <option value="2">FUNCIONARIO</option>
                    <option value="3">ADMINISTRADOR</option>
                </select>
                <div v-if="tipo_usuario == 1" class="if-paciente">
                    <label for="">RH</label>
                    <select v-model="rh">
                        <option value="O+">O+</option>
                        <option value="O-">O-</option>
                        <option value="A+">A+</option>
                        <option value="A-">A-</option>
                        <option value="AB+">AB+</option>
                        <option value="AB-">AB-</option>
                        <option value="B+">B+</option>
                        <option value="B-">B-</option>
                    </select>
                    <div class="error" v-if="!$v.rh.required">Este campo es obligatorio</div>
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
                    <input type="text" v-model.trim="$v.id.$model" id="">
                    <div class="error" v-if="!$v.id.minLength">No es una tarjeta valida</div>
                    <div class="error" v-if="!$v.id.maxLength">No es una tarjeta valida</div>
                    <div class="error" v-if="!$v.id.contieneMayuscula">No puede ingresar letras</div>
                    <div class="error" v-if="!$v.id.contieneMinuscula">No puede ingresar letras</div>
                    <div class="error" v-if="!$v.id.noCaracteresEspeciales">No puede ingresar caracteres especiales</div>
                </div>
        </section>

        <footer class="modal-footer">
            <button id="agregar" @click="submitFormulario">AGREGAR USUARIO</button>
        </footer>
        </div>
    </div>
    </transition>
</template>

<script>

import { mapActions } from 'vuex'
import { required,minLength, email, sameAs, maxLength, alphaNum } from 'vuelidate/lib/validators'
import { esFuerte,noCaracteresEspeciales,noNumeros,contieneMayuscula,validacionFecha,contieneMinuscula,noEspacios } from '../validators/validator'
export default {
    name: 'Modal',
    data(){
        return{
            nombre: '',
            apellido: '',
            fecha: '',
            nombreUsuario: '',
            correo: '',
            clave: '',
            confirma: '',
            tipo_usuario: '3',
            rh: '',
            sexo: 'M',
            tId: 1,
            id: '',
        }
    },
    validations(){
        const validaciones = {
            nombre: {
                required,
                minLength: minLength(3),
                noCaracteresEspeciales,
            },
            apellido: {
                required,
                minLength: minLength(3),
                noCaracteresEspeciales,
            },
            fecha:{
                required,
                validacionFecha,
            },
            nombreUsuario:{
                required,
                minLength: minLength(5),
                contieneMayuscula,
                noCaracteresEspeciales: alphaNum,
                noEspacios
            },
            correo: {
                email
            },
            clave:{
                required,
                minLength: minLength(5),
                maxLength: maxLength(8),
                esFuerte,
            },
            confirma: {
                required,
                sameAsClave: sameAs('clave')
            },
            rh:{},
            id:{},
        }
        if(this.tipo_usuario === '1'){
            validaciones.rh = {
                required,
            }
            validaciones.id = {
                required,
                minLength: minLength(8),
                maxLength: maxLength(10),
                noCaracteresEspeciales,
                contieneMayuscula,
                contieneMinuscula,
            }
        }
        return validaciones      
    },
    methods: {
        ...mapActions(['crearUsuario']),
        submitFormulario(){
            this.$v.$touch()
            if (this.$v.$invalid){
                this.$alert('Llene los datos adecuadamente','Error en el formulario','warning')
            } else {
                // Peticion create
                const usuario = {
                'username':this.nombreUsuario,
                'password': this.clave,
                'first_name': this.nombre,
                'last_name': this.apellido,
                'email': this.correo,
                'fecha_nacimiento': this.fecha,
                'rol': parseInt(this.tipo_usuario),
                "activo": true
                }
                var paciente = {}
                if (usuario.rol === 1){
                    paciente = {
                        'usuario_p' : null,
                        'RH': this.rh,
                        'sexo': this.sexo,
                        'numero_identificacion': this.id,
                        'tipo_identificacion': parseInt(this.tId)
                    }
                }
                this.crearUsuario({'usuario': usuario, 'paciente': paciente})
                .then(() => this.$alert('Usuario creado exitosamente','Exito','success'))
                .catch((err) => this.$alert(err,'Ha ocurrido un error','error'))
                this.close()
            }
        },
        close() {
            this.$emit('close');
        },
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
.error{
    color: red;
    font-size: 0.75em;
    margin: 0.5em
}
label{
    margin: 0.5em;
}
</style>