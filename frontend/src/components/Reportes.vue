<template>
    <div class="reporte">
        <h1>REPORTES</h1>
        <div class="filtros">
            <input type="text" placeholder="Buscar Por Usuario" v-model="buscar">
            <select v-model="tipo_usuario">
                        <option value="1">PACIENTE</option>
                        <option value="2">FUNCIONARIO</option>
                        <option value="3">ADMINISTRADOR</option>
                        <option value="todos">TODOS</option>
            </select>
            <select v-model="activo">
                        <option value="activo">ACTIVO</option>
                        <option value="inactivo">INACTIVO</option>
                        <option value="todos">TODOS</option>
            </select>
        </div>
        <table>
                <thead>
                    <th>ID</th><th>NOMBRE</th><th>EMAIL</th><th>USUARIO</th><th>FECHA NACIMIENTO</th><th>ROL</th><th>ACTIVO</th>
                </thead>
                <tr v-for="usuarioL in filtrarPorActivo" :key="usuarioL.id">
                    <td>{{usuarioL.id}}</td>
                    <td>{{usuarioL.first_name}} {{usuarioL.last_name}}</td>
                    <td>{{usuarioL.email}}</td>
                    <td>{{usuarioL.username}}</td>
                    <td>{{usuarioL.fecha_nacimiento}}</td>
                    <td>{{mostrarRol(usuarioL.rol)}}</td>
                    <td>{{usuarioL.activo}}</td>
                </tr>
            </table>
            <div id="paginacion">
                <ul>
                    <button @click="restarPaginacion()" id="anterior">Anterior</button>
                    <button @click="sumarPainacion()" id="siguiente">Siguiente</button>
                </ul>
            </div>
            <JsonExcel :data="JSON.parse(JSON.stringify(this.filtrarPorActivo))">
            Download Data
            </JsonExcel>
    </div>
</template>

<script>
import { mapState } from 'vuex'
import JsonExcel from 'vue-json-excel'
    export default{
        data(){
            return{
                nPaginacion : 7,
                nActual: 0,
                buscar: "",
                tipo_usuario: "todos",
                activo: "todos"
            }
        },
        components:{
            JsonExcel
        },
        computed:{
        ...mapState(['listaUsuarios']),
        indexStart() {
            return this.nActual * this.nPaginacion
        },
        indexEnd() {
            return this.indexStart + this.nPaginacion
        },
        paginated() {
            return this.listaUsuarios.slice(this.indexStart, this.indexEnd)
        },
        filtrarPorUsuario(){
            var lista = this.paginated 
            if(this.buscar==""){
                return lista
            }else{
                return lista.filter((objeto) => objeto.username.toLowerCase().includes(this.buscar.toLowerCase()))
            }
        },
        filtrarPorTipo(){
            var lista = this.filtrarPorUsuario
            if(this.tipo_usuario == "todos")
            {
                return lista
            }else{
                return lista.filter((objeto) => objeto.rol == this.tipo_usuario)
            }
        },
        filtrarPorActivo(){
            var lista = this.filtrarPorTipo
            if(this.activo == "todos"){ 
                return lista.slice(this.indexStart, this.indexEnd)
            }else{
                if(this.activo == "activo"){
                    return lista.filter((objeto) => objeto.activo == true)
                }else{
                    return lista.filter((objeto) => objeto.activo == false)
                }
            }
        }
        },
        methods:{
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

    }
</script>

<style scoped>
    h1{
        float: left;
        margin-left: 1em;
        font-size: 40px;
    }
    .reporte table{
        width: 80%;
        background-color: white;
        text-align: left;
        color: black;
        top: 15%;
        left:11px;
        border-collapse: collapse;
        position: fixed;
    }
    .reporte th,td{
    padding: 15px;
    }
    .reporte  thead{
    background-color: #063146;
    color: white;
    border-bottom: solid 5px black;
    }
    .reporte tr:nth-child(even){
    background-color: #ddd;
    }
    .reporte tr:hover{
    background-color: #063146;
    color: white;
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
    .reporte .filtros{
        float: left;
        margin-left: 2em;
        margin-top: 2em;
        display: inline-block;
    }
    .reporte input{
        margin-left: 3em;
        width: 200px;
        height: 30px;
        background: white;
        border: none;
        font-size: 10pt;
        float: left;
        color: black;
        padding-left: 45px;
        -webkit-border-radius: 5px;
        -moz-border-radius: 5px;
        border-radius: 5px;
        border: black solid 3px;
    }
    .reporte select{
        margin-left: 2em;
        width: 200px;
        height: 38px;
        background: white;
        border: none;
        font-size: 10pt;
        float: left;
        color: black;
        padding-left: 45px;
        -webkit-border-radius: 5px;
        -moz-border-radius: 5px;
        border-radius: 5px;
        border: black solid 3px;
    }
</style>
