<template>
    <div class="parametrizacion">
        <h1>PARAMETRIZACIÓN DE LA APLICACION</h1>
        <button id="agregar" @click="mostrarModal = true">AGREGAR</button>
        <table>
            <thead>
            <th>ID</th>
            <th>NOMBRE</th>
            <th>FECHA INICIO</th>
            <th>FECHA FIN</th>
            <th>VALOR</th>
            <th>ESTADO</th>
        </thead>
        <tr v-for="para in paginated" :key="para.id">
            <td>{{ para.id }}</td>
            <td>{{ para.nombre }}</td>
            <td>{{ para.fecha_inicio }}</td>
            <td>{{ para.fecha_fin }}</td>
            <td>{{ para.valor }}</td>
            <td>{{ para.estado }}</td>
            <td><button id="modificar" @click="modificar(para)"><i class="fa fa-pencil"></i>Modificar</button></td>
            <td><button id="eliminar" @click="eliminar(para.id)"><i class="fa fa-times"></i>Eliminar</button></td>
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

</style>