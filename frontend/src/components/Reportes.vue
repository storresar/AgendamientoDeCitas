<template>
    <div class="reporte">
        <h1>GENERAR LOS REPORTES</h1>
        <input type="text" placeholder="Buscar Por Usuario" v-model="buscar">
        <select v-model="tipo_usuario">
                    <option value="1">PACIENTE</option>
                    <option value="2">FUNCIONARIO</option>
                    <option value="3">ADMINISTRADOR</option>
                </select>
        <table>
                <thead>
                    <th>ID</th><th>NOMBRE</th><th>EMAIL</th><th>USUARIO</th><th>FECHA NACIMIENTO</th><th>ROL</th>
                </thead>
                <tr v-for="usuarioL in filtrarPorTipo" :key="usuarioL.id">
                    <td>{{usuarioL.id}}</td>
                    <td>{{usuarioL.first_name}} {{usuarioL.last_name}}</td>
                    <td>{{usuarioL.email}}</td>
                    <td>{{usuarioL.username}}</td>
                    <td>{{usuarioL.fecha_nacimiento}}</td>
                    <td>{{mostrarRol(usuarioL.rol)}}</td>
                </tr>
            </table>
            <div id="paginacion">
                <ul>
                    <button @click="restarPaginacion()" id="anterior">Anterior</button>
                    <button @click="sumarPainacion()" id="siguiente">Siguiente</button>
                </ul>
            </div>
    </div>
</template>

<script>
import { mapState } from 'vuex'

    export default{
        data(){
            return{
                nPaginacion : 7,
                nActual: 0,
                buscar: "",
                tipo_usuario: ""
            }
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
            return lista.filter((objeto) => objeto.username.toLowerCase().includes(this.buscar.toLowerCase()))
        },
        filtrarPorTipo(){
            var lista = this.filtrarPorUsuario
            console.log(lista)
            return lista.filter((objeto) => objeto.rol == this.tipo_usuario)
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

</style>
