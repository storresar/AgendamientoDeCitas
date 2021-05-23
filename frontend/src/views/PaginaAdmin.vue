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
                    <a onclick="showDivCitas()"><i class="fa fa-address-book"></i>AUDITORIA</a>
                </li>
                <li>
                    <a onclick="showDivModificar()"><i class="fa fa-area-chart"></i>REPORTES Y GRÁFICAS</a>
                </li>
                <li>
                    <a onclick="alert('AQUI HAY UN MENSAJE')"><i class="fa fa-sign-out"></i>CERRAR SESIÓN</a>
                </li>
            </ul>
        </div>
        <div id="verinformacion" class="info">
            <H1>INFORMACION</H1>
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
                <table>
                <thead>
                    <th>ID</th><th>NOMBRE</th><th>EMAIL</th><th>USUARIO</th><th>ROL</th><th>MODIFICAR</th><th>ELIMINAR</th>
                </thead>
                <tr v-for="usuario in listaUsuarios | paginate" :key="usuario.id">
                    <td>{{usuario.id}}</td>
                    <td>{{usuario.first_name}} {{usuario.last_name}}</td>
                    <td>{{usuario.email}}</td>
                    <td>{{usuario.username}}</td>
                    <td>{{usuario.rol}}</td>
                    <td><button id="modificar"><i class="fa fa-pencil"></i>Modificar</button></td>
                    <td><button id="eliminar"><i class="fa fa-times"></i>Eliminar</button></td>
                </tr>
            </table>
            <ul>
                <li v-for="pageNumber in totalPages" v-if="Math.abs(pageNumber - currentPage) < 3 || pageNumber == totalPages - 1 || pageNumber == 0">
                    <a href="#" @click="setPage(pageNumber)"  :class="{current: currentPage === pageNumber, last: (pageNumber == totalPages - 1 && Math.abs(pageNumber - currentPage) > 3), first:(pageNumber == 0 && Math.abs(pageNumber - currentPage) > 3)}">{{ pageNumber+1 }}</a>
                </li>
            </ul>
        </div>
        <div id="auditoria" style="display: none;">
            ESTE ES EL PANEL DE AUDITORIA
        </div>
    </div>
</template>



<script>

import { mapState, mapActions } from 'vuex'

export default {
    data:{
        searchKey: '',
        currentPage: 0,
        itemsPerPage: 1,
        resultCount: 0
    },
    computed:{
        ...mapState(['usuario', 'listaUsuarios']),
        totalPages: function() {
            return Math.ceil(this.resultCount / this.itemsPerPage)
        }
    },
    methods:{
        showDivInfo(){
            document.getElementById('verinformacion').style.display='';
            document.getElementById('usuarios').style.display='none';
        },
        showDivUsuarios(){
            document.getElementById('verinformacion').style.display='None';
            document.getElementById('usuarios').style.display='';
        },
        ...mapActions(['getListaUsuarios']),
        setPage: function(pageNumber) {
            this.currentPage = pageNumber
        },
    },
    mounted(){
        this.getListaUsuarios()
    },
    filters: {
    paginate: function(list) {
            this.resultCount = list.length
            if (this.currentPage >= this.totalPages) {
                this.currentPage = this.totalPages - 1
            }
            var index = this.currentPage * this.itemsPerPage
            return list.slice(index, index + this.itemsPerPage)
        },
    }
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
    padding: 20px;
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
#eliminar{
    background-color: rgb(202, 59, 59);
    color: white;
}
</style>