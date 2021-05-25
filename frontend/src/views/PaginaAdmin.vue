<template>
    <div id="admin">
    <div class="sidebar">
            <header><img src="https://images.vexels.com/media/users/3/144204/isolated/preview/f6d082b22c3fbdc5d2927ff1c7cd57d4-icono-de-edificio-de-hospital-by-vexels.png"></header>
            <ul>
                <li>
                    <a @click="showDivInfo()"><i class="fa fa-info"></i>MI INFORMACIÓN</a>
                </li>
                <li>                   
                    <a @click="showDivUsuarios()"><i class="fa fa-users"></i>GESTIÓN DE USUARIOS</a>
                </li>
                <li>
                    <a onclick="showDivModificar()"><i class="fa fa-calendar"></i>GESTIÓN DE CITAS</a>
                </li>
                <li>
                    <a @click="showDivAuditoria()"><i class="fa fa-address-book"></i>AUDITORIA</a>
                </li>
                <li>
                    <a onclick="showDivModificar()"><i class="fa fa-area-chart"></i>REPORTES Y GRÁFICAS</a>
                </li>
                <li>
                    <a @click="cerrarSesion()"><i class="fa fa-sign-out"></i>CERRAR SESIÓN</a>
                </li>
            </ul>
        </div>
        <div id="verinformacion" class="info">
            <H1>INFORMACIÓN</H1>
            <img src="https://www.softzone.es/app/uploads/2018/04/guest.png" alt="">
            <div class="detalle">
                <table>
                    <tr>
                        <td>NOMBRE:</td>
                        <td>{{usuario.first_name}}</td>
                    </tr>
                    <tr>
                        <td>USUARIO:</td>
                        <td>{{usuario.username}}</td>
                    </tr>
                    <tr>
                        <td>ESTADO:</td>
                        <td>Activo</td>
                    </tr>
                    <tr>
                        <td>CORREO:</td>
                        <td>{{usuario.email}}</td>
                    </tr>
                </table>
            </div>
        </div>
        <div id="usuarios" style="display: none;" class="listaUsu">
                <h1>LISTA DE USUARIOS EN EL SISTEMA</h1>
                <button id="agregar" @click="showModal">AGREGAR USUARIO</button>
                <table>
                <thead>
                    <th>ID</th><th>NOMBRE</th><th>EMAIL</th><th>USUARIO</th><th>FECHA NACIMIENTO</th><th>ROL</th><th>MODIFICAR</th><th>ELIMINAR</th>
                </thead>
                <tr v-for="(usuario, index) in listaUsuarios"
                v-if="index >= nActual*nPaginacion && index < (nActual*nPaginacion)+nPaginacion"
                :key="usuario.id">
                    <td>{{usuario.id}}</td>
                    <td>{{usuario.first_name}} {{usuario.last_name}}</td>
                    <td>{{usuario.email}}</td>
                    <td>{{usuario.username}}</td>
                    <td>{{usuario.fecha_nacimiento}}</td>
                    <td>{{usuario.rol}}</td>
                    <td><button id="modificar" @click="modificar(usuario)"><i class="fa fa-pencil"></i>Modificar</button></td>
                    <td><button id="eliminar" @click="eliminar(usuario.username)"><i class="fa fa-times"></i>Eliminar</button></td>
                </tr>
            </table>
            <div id="paginacion">
                <ul>
                    <button @click="restarPaginacion()" id="anterior">Anterior</button>
                    <button @click="sumarPainacion()" id="siguiente">Siguiente</button>
                </ul>
            </div>
        </div>
            <ModalRegistro v-show="mostrarModal" @close="closeModal"> </ModalRegistro>
            <ModalModificar v-show="mostrarModalModificar" @close="closeModalModificar">
                <template v-slot:body>
                    <label>Nombre:</label>
                    <br>
                    <input type="text" v-model.trim="$v.nombre.$model" id="nombre"  autocomplete="off">
                    <div class="error" v-if="!$v.nombre.required">Este campo es requerido</div>
                    <br>
                    <label>Apellido:</label>
                    <br>
                    <input type="text" v-model.trim="$v.apellido.$model" id="apellido"  autocomplete="off">
                    <div class="error" v-if="!$v.apellido.required">Este campo es requerido</div>
                    <br>
                    <label>Fecha Nacimiento:</label>
                    <br>
                    <input type="date" v-model.trim="$v.fecha.$model" id="fecha">
                    <div class="error" v-if="!$v.fecha.required">Este campo es obligatorio</div>
                    <br>
                    <label for="">Usuario:</label>
                    <br>
                    <input type="text" v-model.trim="$v.username.$model" id="usuario"  autocomplete="off">
                    <div class="error" v-if="!$v.username.required">Este campo requiere minimo 8 caracteres</div>
                    <br>
                    <label for="">Contraseña</label>
                    <br>
                    <input type="password" v-model.trim="$v.clave.$model" id="">
                    <div class="error" v-if="!$v.clave.minLength">Este campo requiere minimo 8 caracteres</div>
                    <br>
                    <label for="">Confima la contraseña</label>
                    <input type="password" v-model.trim="$v.confirma.$model" id="">
                    <div class="error" v-if="!$v.confirma.required">Este campo es obligatorio</div>
                    <div class="error" v-if="!$v.confirma.sameAsClave">Las claves no coinciden</div>
                    <br>
                    <label for="">Tipo Usuario</label>
                    <br>
                        <select v-model="tipo_usuario" @change="isPaciente">
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
                </template>
                <template v-slot:footer>
                    <button id="modificar" @click="botonModificar(usuarioModificar)">MODIFICAR USUARIO</button>
                </template>
            </ModalModificar>
        <div id="auditoria" style="display: none;" class="audi">
                    <h1>AUDITORIA DE LA APLICACIÓN</h1>
                    <table>
                    <thead>
                        <th>ID</th><th>FECHA</th><th>TIPO</th><th>USUARIO AFECTADO</th><th>USUARIO</th><th>IP</th>
                    </thead>
                    <tr v-for="(auditoria, index) in listaAuditoria"
                v-if="index >= nActualAuditoria*nPaginacionAuditoria && index < (nActualAuditoria*nPaginacionAuditoria)+nPaginacionAuditoria"
                :key="auditoria.id">
                        <td>{{auditoria.id}}</td>
                        <td>{{auditoria.fecha}}</td>
                        <td>{{auditoria.tipo}}</td>
                        <td>{{auditoria.usuario_cambio}}</td>
                        <td>{{auditoria.usuario_realiza}}</td>
                        <td>{{auditoria.ip}}</td>
                    </tr>
                    </table>
                     <div id="paginacion">
                <ul>
                    <button @click="restarPaginacionAuditoria()" id="anterior">Anterior</button>
                    <button @click="sumarPaginacionAuditoria()" id="siguiente">Siguiente</button>
                </ul>
            </div>
        </div>
    </div>
</template>



<script>

import { mapState, mapActions } from 'vuex'
import ModalRegistro from '../components/ModalRegistro.vue'
import ModalModificar from '../components/ModalModificar.vue'
import { required,minLength, sameAs } from 'vuelidate/lib/validators'
export default {
    data(){
        return{
            nPaginacion : 4 ,
            nActual: 0,
            nPaginacionAuditoria : 8 ,
            nActualAuditoria: 0,
            mostrarModal: false,
            mostrarModalModificar: false,
            usuarioModificar: '',
            nombre: '',
            apellido: '',
            fecha: '',
            tipo_usuario: '',
            username: '',
            clave:'',
            confirma:'',
            rh: '',
            sexo: '',
            tId: 1,
            id: '',
            correo: ''
        }
    },
    components:{
        ModalRegistro,
        ModalModificar
    },
    validations(){
        if(this.tipo_usuario === '1'){
            return{
                nombre: {
                    required
                },
                apellido: {
                    required
                },
                fecha:{
                    required
                },
                username:{
                    required
                },
                clave:{
                    required,
                    minLength: minLength(8)
                },
                confirma: {
                    required,
                    sameAsClave: sameAs('clave')
                },
                rh: {
                    required,
                },
                id: {
                    required,
                },
            }
        }else{
            return{
                nombre: {
                    required
                },
                apellido: {
                    required
                },
                fecha:{
                    required
                },
                username:{
                    required
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
        }
    },
    computed:{
        ...mapState(['usuario', 'listaUsuarios','listaAuditoria']),
    },
    methods:{
        cerrarSesion(){
            window.localStorage.clear()
            this.$router.push({name:'Home'})
        },
        showDivInfo(){
            document.getElementById('verinformacion').style.display='';
            document.getElementById('usuarios').style.display='None';
            document.getElementById('auditoria').style.display='None';
        },
        showDivUsuarios(){
            document.getElementById('verinformacion').style.display='none';
            document.getElementById('usuarios').style.display='';
            document.getElementById('auditoria').style.display='none';
        },
        showDivAuditoria(){
            document.getElementById('verinformacion').style.display='None';
            document.getElementById('usuarios').style.display='None';
            document.getElementById('auditoria').style.display='';
        },
        ...mapActions(['getListaUsuarios','eliminarUsuario','modificarUsuario','getAuditoria']),
        restarPaginacion(){
            if(this.nActual > 0){
                this.nActual--;
            }
        },
        sumarPainacion(){
            if((this.nActual*this.nPaginacion)+this.nPaginacion < this.listaUsuarios.length){
                this.nActual++;
            }
        },
        restarPaginacionAuditoria(){
            if(this.nActualAuditoria > 0){
                this.nActualAuditoria--;
            }
        },
        sumarPaginacionAuditoria(){
            if((this.nActualAuditoria*this.nPaginacionAuditoria)+this.nPaginacionAuditoria < this.listaAuditoria.length){
                this.nActualAuditoria++;
            }
        },
        eliminar(usuario){
            this.eliminarUsuario(usuario)
            .then(msg => this.$alert(msg,'Usuario elminado correctamente','success'))
            .catch(msg => this.$alert(msg,'Ha ocurrido un error','warning'))
        },
        showModal() {
            this.mostrarModal = true;
        },
        closeModal() {
            this.mostrarModal = false;
        },
        showModalModificar() {
            this.mostrarModalModificar = true;
        },
        closeModalModificar() {
            this.mostrarModalModificar = false;
        },
        modificar(usuario){
            this.nombre = usuario.first_name
            this.apellido = usuario.last_name
            this.fecha = usuario.fecha_nacimiento
            this.username = usuario.username
            this.correo = usuario.email
            if(usuario.rol === 1){
                this.tipo_usuario = '1'
            }else if(usuario.rol === 2) {
                this.tipo_usuario = '2'
            }else{
                this.tipo_usuario = '3'
            }
            this.showModalModificar()
            this.usuarioModificar = usuario
        },
        botonModificar(usuarioNuevo){
            this.$v.$touch()
            if (this.$v.$invalid){
                this.$alert('Llene los datos adecuadamente','Error en el formulario','warning')
            } else{
                const usuario = {
                'username':this.usuario,
                'password': this.clave,
                'first_name': this.nombre,
                'last_name': this.apellido,
                'email': this.correo,
                'fecha_nacimiento': this.fecha,
                'rol': parseInt(this.tipo_usuario),
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
                this.usuarioModificar = usuarioNuevo
                
                this.modificarUsuario({'usuario': usuario, 'paciente': paciente})
                .then(msg => this.$alert(msg,'Usuario modificado correctamente','success'))
                .catch(msg => this.$alert(msg,'Ha ocurrido un error','warning'))
                this.mostrarModalModificar = false;
            }
        },
    },
    mounted(){
        this.getListaUsuarios()
        this.getAuditoria()
    },
}
</script>


<style scoped> 
@import url('https://fonts.googleapis.com/css2?family=Karla:ital,wght@1,300&display=swap');
#admin{
    font-family: 'Karla', sans-serif;
}

.sidebar{
    position: fixed;
    right: 0;
    top: 0;
    width: 250px;
    height: 100%;
    background-color:#042331;
}
.sidebar ul{
    padding: 0;
}

.sidebar header{
    font-size: 22px;
    color: white;
    text-align: center;
    line-height: 70px;
    background: #063146;
    user-select: none;
}
.sidebar header img{
    width: 150px;
    height: 150px; 
    
}
.sidebar ul a{
    display: block;
    width: 100%;
    height: 100%;
    line-height: 67px;
    font-size: 15px;
    color: white;
    padding-left: 0px;
    box-sizing: border-box;
    border-top: 1px solid rgba(255, 255, 255,.1);
    border-bottom: 1px solid black;
    transition: .4s;
    text-align: left;
    padding-left: 20px;
}
.sidebar li{
    list-style: none;
    text-decoration: none;
}
ul li:hover a{
    padding-left: 50px;
    cursor: pointer;
}
.sidebar ul a i{
    margin-right: 16px;
    background: transparent;
}
.sidebar img{
    background: transparent;
}
.info{
    position: fixed;
    max-height: 40em;
    width: 30%;
    right: 45%;
    top: 5%;
    background-color: darkcyan;
    border-radius: 10%;
}
.info h1{
    text-align: center;
    line-height: 100px;
}
.info img{
    display:block;
    margin:auto;
    border-radius: 50%;
    height: 200px;
    width: 200px;
}
.info .detalle table{
    width: 100%;
    font-size: 22px;
    margin-top: 2%;
    color:beige;
    margin-bottom: 1em;
    line-height: 30%;
}
.listaUsu h1{
    text-align: left;
    padding-left: 30px;
}
.listaUsu #agregar{
    background-color: rgb(20, 149, 158);
    color: white;
    border: none;
    padding: 20px;
    border-radius: 6px;
    font-family: 'Karla', sans-serif;
    font-size: 15px;
    width: 300px;
    position: relative;
    left: 17em;
    top: -3em;
}
.listaUsu #agregar:hover{
    background-color: rgb(38, 193, 204);
}
.listaUsu table{
    width: 80%;
    background-color: white;
    text-align: left;
    color: black;
    top: 20%;
    left:11px;
    border-collapse: collapse;
    position: fixed;
}
.listaUsu th,td{
    padding: 15px;
}
.listaUsu thead{
    background-color: #063146;
    color: white;
    border-bottom: solid 5px black;
}
.listaUsu tr:nth-child(even){
    background-color: #ddd;
}
.listaUsu tr:hover{
    background-color: #063146;
    color: white;
}
.listaUsu button{
    width: 100%;
    border: none;
    padding: 10px;
    border-radius: 6px;
    font-family: 'Karla', sans-serif;
    font-size: 15px;
}
.listaUsu button i{
    margin-right: 16px;
}
#modificar{
    background-color: rgb(20, 94, 20);
    color: white;
}
#modificar:hover{
    background-color: rgb(23, 158, 23);
}
#eliminar{
    background-color: rgb(202, 59, 59);
    color: white;
}
#eliminar:hover{
    background-color: rgb(207, 6, 6);
}
#paginacion button {
    background-color: black;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 6px;
    font-family: 'Karla', sans-serif;
    font-size: 15px;
    width: 100px;
}

#paginacion #anterior{
    position: fixed;
    top: 90%;
    left: 30%;
}

#paginacion #siguiente{
    position: fixed;
    top: 90%;
    left: 40%;
}
#paginacion button:hover{
    background-color: gray;
    color: white;
}
.audi h1{
    text-align: left;
    padding-left: 30px;
}

.audi table{
    width: 80%;
    background-color: white;
    text-align: left;
    color: black;
    top: 20%;
    left:11px;
    border-collapse: collapse;
    position: fixed;
}

.audi th,td{
    padding: 15px;
}
.audi thead{
    background-color: #063146;
    color: white;
    border-bottom: solid 5px black;
}
.audi tr:nth-child(even){
    background-color: #ddd;
}
.audi tr:hover{
    background-color: #063146;
    color: white;
}
</style>