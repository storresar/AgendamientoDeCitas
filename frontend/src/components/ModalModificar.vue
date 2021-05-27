<template>
<transition name="modal-fade">
    <div class="modal-backdrop">
        <div class="modal">
        <header class="modal-header">
            <strong>MODIFICAR USUARIO</strong>
            <button
            type="button"
            class="btn-close"
            @click="close"
            >X</button>
        </header>

        <section class="modal-body">
            <label for="">Usuario:</label>
            <input type="text" v-model.trim="$v.nombreUsuario.$model" id="usuario"  autocomplete="off">
            <div class="error" v-if="!$v.nombreUsuario.required">Este campo requiere minimo 8 caracteres</div>
            <label for="">Correo:</label>
            <input type="text" v-model.trim="$v.correo.$model" id="usuario"  autocomplete="off">
            <div class="error" v-if="!$v.correo.email">Este correo es invalido</div>
            <label>Nombre:</label>
            <input type="text" v-model.trim="$v.nombre.$model" id="nombre"  autocomplete="off">
            <div class="error" v-if="!$v.nombre.required">Este campo es requerido</div>
            <label>Apellido:</label>
            <input type="text" v-model.trim="$v.apellido.$model" id="apellido"  autocomplete="off">
            <div class="error" v-if="!$v.apellido.required">Este campo es requerido</div>
            <label>Fecha Nacimiento:</label>
            <input type="date" v-model.trim="$v.fecha.$model" id="fecha">
            <div class="error" v-if="!$v.fecha.required">Este campo es obligatorio</div>
            <label for="">Contraseña</label>
            <input type="password" v-model.trim="$v.clave.$model" id="">
            <div class="error" v-if="!$v.clave.minLength">Este campo requiere minimo 8 caracteres</div>
            <label for="">Confima la contraseña</label>
            <input type="password" v-model.trim="$v.confirma.$model" id="">
            <div class="error" v-if="!$v.confirma.required">Este campo es obligatorio</div>
            <div class="error" v-if="!$v.confirma.sameAsClave">Las claves no coinciden</div>
            <label for="">Estado Usuario</label>
            <input type="checkbox" name="" id="" v-model="estado">
            <label for="">Tipo Usuario</label>
            <select v-model="tipo_usuario" @change="changePaciente()">
                <option value="1">PACIENTE</option>
                <option value="2">FUNCIONARIO</option>
                <option value="3">ADMINISTRADOR</option>
            </select>
            <div v-if="tipo_usuario == 1" class="if-paciente">
                <label for="">RH</label>
                <input type="text" v-model.trim="$v.rh.$model" id="">
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
                <div class="error" v-if="!$v.id.required">Este campo es obligatorio</div>
            </div>
        </section>

        <footer class="modal-footer">
            <button id="agregar" @click="submitFormulario()">MODIFICAR USUARIO</button>
        </footer>

        </div>
    </div>
    </transition>
</template>

<script>
import { required,minLength, sameAs, email } from 'vuelidate/lib/validators'
import { mapActions } from 'vuex'
 
export default {
    name: 'Modal',
    props: ['usuario', 'paciente'],
    data() {
        return {
            nombre: this.usuario.first_name,
            apellido: this.usuario.last_name,
            fecha: this.usuario.fecha_nacimiento,
            tipo_usuario: String(this.usuario.rol),
            nombreUsuario: this.usuario.username,
            correo: this.usuario.email,
            estado: this.usuario.activo,
            clave:'Gambito1',
            confirma:'Gambito1',
            rh: this.paciente.RH,
            sexo: this.paciente.sexo,
            tId: this.paciente.tipo_identificacion,
            id: this.paciente.numero_identificacion,
            isPaciente: false,
        }
    },
    methods: {
        ...mapActions(['modificarUsuario']),
        close() {
            this.$emit('close');
        },
        botonModificar(usuarioNuevo){
            this.$v.$touch()
            if (this.$v.$invalid){
                this.$alert('Llene los datos adecuadamente','Error en el formulario','warning')
            }
        },
        changePaciente(){
            this.isPaciente = false
            if (this.tipo_usuario === '1') {
                this.isPaciente = true
            }
        },
        submitFormulario(){
            this.$v.$touch()
            if (this.$v.$invalid){
                this.$alert('Llene los datos adecuadamente','Error en el formulario','warning')
            } else {
                // Peticion PUT
                this.usuario.email = this.correo
                this.usuario.password = this.clave
                this.usuario.first_name = this.nombre
                this.usuario.last_name = this.apellido
                this.usuario.fecha_nacimiento = this.fecha
                this.usuario.rol = parseInt(this.tipo_usuario)
                this.usuario.activo = this.estado
                if (this.usuario.rol === 1){
                    this.paciente.usuario_p = this.usuario.id
                    this.paciente.RH = this.rh
                    this.paciente.sexo = this.sexo
                    this.paciente.numero_identificacion = this.id
                    this.paciente.tipo_identificacion = parseInt(this.tId)
                }
                this.modificarUsuario({'usuario': this.usuario, 'paciente': this.paciente})
                .then(() => this.$alert('Usuario modificado exitosamente','Exito','success'))
                .catch((err) => this.$alert(err,'Ha ocurrido un error','error'))
                this.close()
            }
        },
    },
    validations(){
        const validaciones = {
            nombre: {
                required,
                minLength: minLength(3)
            },
            apellido: {
                required,
                minLength: minLength(3),
            },
            fecha:{
                required
            },
            nombreUsuario:{
                required,
                minLength: minLength(8),
            },
            correo: {
                email
            },
            clave:{
                required,
                minLength: minLength(8)
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
            }
        }
        return validaciones  
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
</style>