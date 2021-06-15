<template>
    <div id="admin">
    <div class="sidebar">
            <header><img src="@/assets/logocitas.png"></header>
            <ul>
                <li>
                    <a @click="showDivInfo()"><i class="fa fa-info"></i>MI INFORMACIÓN</a>
                </li>
                <li>                   
                    <a @click="showDivUsuarios()"><i class="fa fa-users"></i>GESTIÓN DE USUARIOS</a>
                </li>
                <li>
                    <a @click="showDivAuditoria()"><i class="fa fa-address-book"></i>AUDITORIA</a>
                </li>
                <li>
                    <a @click="showDivGraficas()"><i class="fa fa-area-chart"></i>GRÁFICAS</a>
                </li>
                <li>
                    <a @click="showDivReportes()"><i class="fa fa-file-text-o"></i>REPORTES</a>
                </li>
                <li>
                    <a @click="showDivPara()"><i class="fa fa-cog"></i>PARAMETRIZACIÓN</a>
                </li>
                <li>
                    <a @click="cerrarSesion()"><i class="fa fa-sign-out"></i>CERRAR SESIÓN</a>
                </li>
            </ul>
        </div>
        <div id="verinformacion" class="info">
            <h1>INFORMACIÓN</h1>
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
        
        <div id="graficas" v-if="mostrarGraficas" class="">
            <GraficasPadre/>
        </div>
        <div id="usuarios" style="display: none;" class="listaUsu">
                <h1>LISTA DE USUARIOS EN EL SISTEMA</h1>
                <button id="agregar" @click="mostrarModal = true"><i class="fa fa-plus-circle"> </i> Agregar</button>
                <table>
                <thead>
                    <th>Id</th><th>Nombre</th><th>Email</th><th>Usuario</th><th>Fecha Nacimiento</th><th>Rol</th><th></th><th></th>
                </thead>
                <tr v-for="usuarioL in paginated" :key="usuarioL.username">
                    <td>{{usuarioL.id}}</td>
                    <td>{{usuarioL.first_name}} {{usuarioL.last_name}}</td>
                    <td>{{usuarioL.email}}</td>
                    <td>{{usuarioL.username}}</td>
                    <td>{{usuarioL.fecha_nacimiento}}</td>
                    <td>{{mostrarRol(usuarioL.rol)}}</td>
                    <td><button id="modificar" @click="modificar(usuarioL)"><i class="fa fa-pencil"></i> <div id="texto">Modificar</div> </button></td>
                    <td><button id="eliminar" @click="eliminar(usuarioL.username)"><i class="fa fa-times"></i><div id="texto">Eliminar</div></button></td>
                </tr>
                <tfoot>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td>
                        <button @click="restarPaginacion()" id="anterior">Anterior</button>
                    </td>
                    <td>
                        <button @click="sumarPainacion()" id="siguiente">Siguiente</button>
                    </td>
                    <td></td>
                    <td></td>
                </tfoot>
            </table>
        </div>
        <ModalRegistro v-show="mostrarModal" @close="mostrarModal = false"/>
        <ModalModificar
        v-if="mostrarModalModificar"
        @close="mostrarModalModificar = false"
        :usuario="usuarioModificar"
        :paciente="pacienteModificar"/>
        <div v-if="mostrarAuditoria" class="audi">
                    <h1>AUDITORIA DE LA APLICACIÓN</h1>
                    <table>
                    <thead>
                        <th>Id</th><th>Fecha</th><th>Tipo</th><th>Usuario Afectado</th><th>Usuario</th><th>IP</th>
                    </thead>
                    <tr v-for="auditoria in paginatedA" :key="auditoria.fecha">
                        <td>{{auditoria.id}}</td>
                        <td>{{auditoria.fecha.substring(0,10)}}</td>
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
        <div id="reportes" style="display: none;">
            <Reportes/>
        </div>
        <div id="parametrizacion" style="display: none;">
            <Parametrizacion/>
        </div>
        
    </div>
</template>



<script>

import { mapState, mapActions } from 'vuex'
import ModalRegistro from '../components/ModalRegistro.vue'
import ModalModificar from '../components/ModalModificar.vue'
import GraficasPadre from '../components/GraficasPadre.vue'
import Reportes from '../components/Reportes.vue'
import Parametrizacion from '../components/Parametrizacion.vue'
export default {
    data(){
        return{
            nPaginacion : 6 ,
            nActual: 0,
            nPaginacionAuditoria : 8 ,
            nActualAuditoria: 0,
            mostrarModal: false,
            mostrarModalModificar: false,
            usuarioModificar : '',
            pacienteModificar : '',
            mostrarGraficas: false,
            mostrarAuditoria: false
        }
    },
    components:{
        ModalRegistro,
        ModalModificar,
        GraficasPadre,
        Reportes,
        Parametrizacion
    },

    computed:{
        ...mapState(['usuario', 'listaUsuarios','listaAuditoria', 'paciente','getAuditoria']),
        indexStart() {
            return this.nActual * this.nPaginacion
        },
        indexEnd() {
            return this.indexStart + this.nPaginacion
        },
        paginated() {
            return this.listaUsuarios.slice(this.indexStart, this.indexEnd)
        },
        indexAStart() {
            return this.nActualAuditoria * this.nPaginacionAuditoria
        },
        indexAEnd() {
            return this.indexAStart + this.nPaginacionAuditoria
        },
        paginatedA() {
            return this.listaAuditoria.slice(this.indexAStart, this.indexAEnd)
        }
    },
    methods:{
        ...mapActions(['getPaciente','getListaUsuarios','eliminarUsuario','modificarUsuario','getAuditoria','getParametrizacion']),
        cerrarSesion(){
            window.localStorage.clear()
            this.$router.push({name:'Home'})
        },
        showDivInfo(){
            document.getElementById('verinformacion').style.display='';
            this.mostrarAuditoria = false
            document.getElementById('reportes').style.display='None';
            document.getElementById('parametrizacion').style.display='None';
            this.mostrarGraficas = false
        },
        showDivUsuarios(){
            document.getElementById('verinformacion').style.display='none';
            document.getElementById('usuarios').style.display='';
            this.mostrarAuditoria = false
            document.getElementById('reportes').style.display='None';
            document.getElementById('parametrizacion').style.display='None';
            this.mostrarGraficas = false
        },
        showDivAuditoria(){
            document.getElementById('verinformacion').style.display='None';
            document.getElementById('usuarios').style.display='None';
            document.getElementById('auditoria').style.display='';
            document.getElementById('reportes').style.display='None';
            document.getElementById('parametrizacion').style.display='None';
            this.mostrarGraficas = false
            this.getAuditoria()
            .then(() => this.mostrarAuditoria = true)
        },
        showDivGraficas(){
            document.getElementById('verinformacion').style.display='None';
            document.getElementById('usuarios').style.display='None';
            this.mostrarAuditoria = false
            document.getElementById('reportes').style.display='None';
            document.getElementById('parametrizacion').style.display='None';
            this.mostrarGraficas = true
        },
        showDivReportes(){
            document.getElementById('verinformacion').style.display='None';
            document.getElementById('usuarios').style.display='None';
            this.mostrarAuditoria = false
            document.getElementById('reportes').style.display='';
            document.getElementById('parametrizacion').style.display='None';
            this.mostrarGraficas = false
        },
        showDivPara(){
            document.getElementById('verinformacion').style.display='None';
            document.getElementById('usuarios').style.display='None';
            this.mostrarAuditoria = false
            document.getElementById('reportes').style.display='None';
            document.getElementById('parametrizacion').style.display='';
            this.mostrarGraficas = false
        },
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
            .catch(msg => this.$alert(msg,'Ha ocurrido un error','error'))
        },
        modificar(usuario){
            this.usuarioModificar = usuario
            console.log(this.usuarioModificar)
            if (this.usuarioModificar.rol === 1) {
                this.getPaciente(this.usuarioModificar.id)
                .then(() => {
                    this.pacienteModificar = this.paciente
                    this.mostrarModalModificar = true
                })
                .catch(msg => {
                    this.$alert(msg,'Ha ocurrido un error','error')
                    this.mostrarModalModificar = false
                })
            } else {
                this.pacienteModificar = {
                    RH : '',
                    sexo: 'M',
                    numero_identificacion : '',
                    tipo_identificacion: '',
                    usuario_p: this.usuarioModificar.id,
                }
                this.mostrarModalModificar = true
            }
        },
        mostrarRol(rol){
            if(rol == 1){
                return "PACIENTE"
            }else if(rol == 2){
                return "FUNCIONARIO"
            }else{
                return "ADMIN"
            }
        }
    },
    mounted(){
        this.getListaUsuarios()
        this.getAuditoria()
        this.getParametrizacion()
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
    width: 19%;
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
    width: 250px;
    height: 130px; 
}
.sidebar ul a{
    display: block;
    width: 100%;
    height: 100%;
    line-height: 60px;
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
    float: left;
    font-family: 'Lato', sans-serif; font-size: 30px; font-weight: 300; 
    margin-left: 1em;
    text-transform: uppercase;
    text-align: left;
}
.listaUsu #agregar{
    background-color: rgb(20, 149, 158);
    color: white;
    border: none;
    position: relative;
    margin-top: 1%;
    margin-bottom: 1%;
    left: -5%;
    border-radius: 6px;
    font-family: 'Karla', sans-serif;
    font-size: 18px;
    width: 25%;
}
.listaUsu #agregar:hover{
    background-color: rgb(38, 193, 204);
}
.listaUsu table{
    width: 80%;
    background-color: white;
    text-align: left;
    color: black;
    top: 15%;
    left:11px;
    border-collapse: collapse;
    position: relative;
    font-size: 18px;
}
.listaUsu th,td{
    padding: 1.5%;
}
.listaUsu thead{
    font-size: 100%;
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
    border-radius: 6px;
    font-family: 'Karla', sans-serif;
}
#texto{
    float: right;
    font-size: 14px;
}
@media screen and (max-width: 1600px)
{
    #texto{
        display: none;
        
    }
    #modificar{
        font-size: 150%;
    }

    #eliminar{
        font-size: 150%;
    }
    .listaUsu table{
        font-size: 90%;
    }
}
.listaUsu button i{
    margin-right: 0px;
}
#modificar{
    padding: 10%;
    background-color: rgb(20, 94, 20);
    color: white;
}
#modificar:hover{
    background-color: rgb(23, 158, 23);
}
#eliminar{
    padding: 10%;
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
#siguiente, #anterior{
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
    position: relative;
    top: 90%;
    left: -10%;
}

#paginacion #siguiente{
    position: relative;
    top: 90%;
    left: -5%;
}
#paginacion button:hover{
    background-color: gray;
    color: white;
}
tfoot{
    background-color: grey;
}
.audi h1{
    font-family: 'Lato', sans-serif; font-size: 30px; font-weight: 300; 
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