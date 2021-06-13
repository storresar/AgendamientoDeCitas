<template>
<transition name="modal-fade">
    <div class="modal-backdrop">
        <div class="modal">
        <header class="modal-header">
            <strong>AGREGAR PARAMETRO</strong>
            <button
            type="button"
            class="btn-close"
            @click="close"
            >X</button>
        </header>
        <section class="modal-body">
            <label>Nombre:</label>
            <select v-model="nombre">
                    <option value="admin">ADMINISTRADORES PERMITIDOS</option>
                    <option value="correo">MENSAJE DE CORREO ELECTRONICO</option>
                    <option value="inactivar">DIAS DE INACTIVIDAD DE USUARIO</option>
            </select>
            <label>Fecha de inicio:</label>
            <input type="date" v-model.trim="$v.fecha_ini.$model" id="fecha">
            <label>Fecha de fin:</label>
            <input type="date" v-model.trim="$v.fecha_fin.$model" id="fecha">
            <label>Valor</label>
            <div v-if="nombre == 'correo'">
                <input type="text" v-model.trim="$v.valor.$model" id="usuario"  autocomplete="off">
            </div>
            <div v-if="nombre != 'correo'">
                <input type="number" v-model.trim="$v.valor.$model" id="usuario" min="0" autocomplete="off">
                <div class="error" v-if="!$v.valor.espositivo">Solo se puede con numeros positivos</div>
            </div>
        </section>

        <footer class="modal-footer">
            <button id="agregar" @click="submitFormulario()">REGISTRAR PARAMETRO</button>
        </footer>

        </div>
    </div>
    </transition>
</template>

<script>
    import { required } from 'vuelidate/lib/validators'
    import { espositivo } from '../../validators/validator'
    import { mapActions } from 'vuex'
export default {
    name: 'AGREGAR',
    data(){
        return{
            nombre: '',
            fecha_ini : '',
            fecha_fin : '',
            valor : '',
            parametro: ''
        }
    },
    methods:{
        ...mapActions(['crearParametrizacion']),
        close() {
            this.$emit('close');
        },
        submitFormulario(){
            this.$v.$touch()
            if (this.$v.$invalid){
                this.$alert('Llene los datos adecuadamente','Error en el formulario','warning')
            } else {
                const parametro = {
                    'nombre' : this.nombre,
                    'fecha_inicio' : this.fecha_ini,
                    'fecha_fin' : this.fecha_fin,
                    'valor' : this.valor
                }
                this.crearParametrizacion(parametro)
                .then(() => this.$alert('Parametro creado exitosamente','Exito','success'))
                .catch((err) => this.$alert(err,'Ha ocurrido un error','error'))
                this.close()
            }
        }
    },
    validations(){
        
            var validaciones = {
                nombre: {
                required
                },
                fecha_ini: {
                    required
                },
                fecha_fin:{
                    required
                },
                valor:{
                    required,
                }
            }
            
            if(this.nombre != 'correo'){
                validaciones.valor = {
                    required,
                    espositivo
                }
            }
            return validaciones
    }
}
</script>
<style scoped>
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