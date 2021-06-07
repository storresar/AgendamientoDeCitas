<template>
    <div class="parametrizacion">
        <h1>PARAMETRIZACIÓN DE LA APLICACION</h1>
        <button id="agregar" @click="mostrarModal = true"><i class="fa fa-plus-circle"></i>AGREGAR</button>
        <table>
            <thead>
            <th>MODIFICAR</th>
            <th>ELIMINAR</th>
            <th>ID</th>
            <th>NOMBRE</th>
            <th>FECHA INICIO</th>
            <th>FECHA FIN</th>
            <th>VALOR</th>
            <th>ESTADO</th>
        </thead>
        <tr v-for="para in paginated" :key="para.id">
            <td><button id="modificar" @click="modificar(para)"><i class="fa fa-pencil"></i>Modificar</button></td>
            <td><button id="eliminar" @click="eliminar(para)"><i class="fa fa-times"></i>Eliminar</button></td>
            <td>{{ para.id }}</td>
            <td>{{ para.nombre }}</td>
            <td>{{ para.fecha_inicio }}</td>
            <td>{{ para.fecha_fin }}</td>
            <td>{{ para.valor }}</td>
            <div v-if="para.estado == true">
                <td><i class="fa fa-check-circle-o" aria-hidden="true" id="activo"></i> ACTIVO</td>
            </div>
            <div v-if="para.estado == false">
                <td><i class="fa fa-times-circle-o" aria-hidden="true" id="inactivo"></i> INACTIVO</td>
            </div>
        </tr>
        </table>
        <div id="paginacion">
        <ul>
            <button @click="restarPaginacion()" id="anterior">Anterior</button>
            <button @click="sumarPainacion()" id="siguiente">Siguiente</button>
        </ul>
        </div>
            <RegistroParametro v-show="mostrarModal" @close="mostrarModal = false"/>
            <ModificarParametro
            v-if="mostrarModalModificar"
            @close="mostrarModalModificar = false"
            :parametro="parametroModificar"/>
    </div>
</template>

<script>
import { mapState,mapActions } from "vuex";
import ModificarParametro from '../components/ModalesParametros/ModificarParametro.vue'
import RegistroParametro from '../components/ModalesParametros/RegistroParametro.vue'
export default {
    data(){
        return{
            nPaginacion: 7,
            nActual: 0,
            parametroModificar : '',
            mostrarModalModificar: false,
            mostrarModal: false
        }
    },
    components:{
        ModificarParametro,
        RegistroParametro
    },
    methods:{
        ...mapActions(["eliminarParametrizacion"]),
        eliminar(parametrizacion){
            this.eliminarParametrizacion(parametrizacion)
            .then(msg => this.$alert(msg,'Parametro elminado correctamente','success'))
            .catch(msg => this.$alert(msg,'Ha ocurrido un error','error'))
        },
        modificar(parametrizacion){
            this.parametroModificar = parametrizacion
            this.mostrarModalModificar = true
        }

    },
    computed:{
        ...mapState(["listaParametrizacion"]),
        indexStart() {
            return this.nActual * this.nPaginacion;
        },
        indexEnd() {
            return this.indexStart + this.nPaginacion;
        },
        paginated() {
            return this.listaParametrizacion.slice(this.indexStart, this.indexEnd);
        },
    }
}
</script>

<style scoped>
    .parametrizacion table{
    width: 80%;
    background-color: rgb(85, 82, 82);
    text-align: left;
    color: white;
    top: 20%;
    left:11px;
    border-collapse: collapse;
    border: 1px solid black;
    position: fixed;
    }
    .parametrizacion th,td{
    padding: 15px;
    }
    .parametrizacion thead{
    background-color: #000000;
    color: white;
    border-bottom: solid 5px black;
    }
    .parametrizacion button{
    width: 100%;
    border: none;
    padding: 10px;
    font-family: 'Karla', sans-serif;
    font-size: 15px;
    }
    .parametrizacion button i{
    margin-right: 16px;
    }
    #modificar{
    background-color: rgb(123, 131, 9);
    color: white;
    }
    #eliminar{
    background-color: rgb(202, 59, 59);
    color: white;
    }
    #eliminar:hover{
    background-color: rgb(207, 6, 6);
    }
    #modificar:hover{
    background-color: rgb(206, 219, 17);
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
        cursor: pointer;
    }
    #agregar{
    background-color: rgb(0, 0, 0);
    color: white;
    border: none;
    padding: 20px;
    border-radius: 6px;
    font-family: 'Karla', sans-serif;
    font-size: 15px;
    width: 300px;
    position: fixed;
    left: 2em;
    top: 6em;
    }
    #agregar:hover{
    background-color: rgb(109, 128, 129);
    cursor: pointer;
    }
    #activo{
        color: rgb(30, 212, 30);
    }
    #inactivo{
        color: rgb(190, 34, 34);
    }
</style>