<template>
    <div class="componente">
        <div class="info-general hijo">
            <div class="carta-info">
                <p><strong>Cantidad de usuarios</strong></p>
                <div class="valor">{{cUsuarios}}</div>
                <div class="subtitulos">
                    <div class="right"><strong>Total Inactivos: {{cInactivos}}</strong></div>
                    <div><strong>Total Activos: {{cActivos}}</strong></div>
                </div>
            </div>
            <div class="carta-info">
                <p><strong>Cantidad de doctores</strong></p>
                <div class="valor">{{cDoctores}}</div>
            </div>
            <div class="carta-info">
                <p><strong>Cantidad de citas</strong></p>
                <div class="valor">{{cCitas}}</div>
            </div>
        </div>
        <div class="grafica-fila1 hijo">
            <div class="carta-info">
                <CantidadUsuariosPorTiempo/>
            </div>
            <div class="carta-info">
                <CantidadTipoUsuarios/>
            </div>
        </div>
        <div class="grafica-fila2 hijo">
            <div class="carta-info">
                <MujeresVsHombres/>
            </div>
            <div class="carta-info">
                <ActivosVsInactivos/>
            </div>
            <div class="carta-info">
                <CantidadTipoUsuarios/>
            </div>
        </div>
    </div>
</template>

<script>

import { mapState } from 'vuex'
import ActivosVsInactivosVue from './Graficas/ActivosVsInactivos.vue'

export default {
    name:'GraficasPadre',
    components: {
        CantidadTipoUsuarios : () => import('./Graficas/CantidadTipoUsuarios.vue'),
        CantidadUsuariosPorTiempo : () => import('./Graficas/CantidadUsuariosPorTiempo.vue'),
        MujeresVsHombres : () => import('./Graficas/MujeresVsHombres.vue'),
        ActivosVsInactivos : () => import('./Graficas/ActivosVsInactivos.vue')
    },
    data(){
        return{
            cUsuarios: 0,
            cDoctores: 0,
            cCitas: 0,
            cActivos: 0,
            cInactivos: 0,
        }
    },
    computed:{
        ...mapState(['listaUsuarios'])
    },
    methods: {
        calcularValores(){
            this.cUsuarios = this.listaUsuarios.length
            for (let i = 0; i < this.listaUsuarios.length; i++) {
                if(this.listaUsuarios[i].activo === true){
                    this.cActivos++
                } else {
                    this.cInactivos++
                }
            }
        },
    },
    mounted(){
        this.calcularValores()
    }
}
</script>

<style scoped>
.componente{
    display: grid;
    grid-template-rows: 20vh 80vh 60vh;
    grid-template-columns: 100vw;
    grid-gap: 1em;
    background-color: #F0F2F4;
    overflow: auto;
    margin-right: 250px;
    
}
.hijo{
    background-color: #F0F2F4;
    margin: 1em;
    margin-right: 290px;
}
.grafica-fila1{
    display: grid;
    grid-gap: 2em; 
    grid-template-columns: 59% 38%;
}
.grafica-fila2{
    display: grid;
    grid-gap: 2em; 
    grid-template-columns: 31.2% 31.2% 31.2%;
}
.info-general{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 1em;
}
.carta-info{
    background-color: rgb(144, 185, 221);
    text-align: left;
    border-radius: 1em;
}   
.carta-info p{

    margin: 0;
    margin-top: 1em;
    margin-left: 1em;
    padding: 0;
    font-size: 1.2em;
}
.carta-info .valor{
    padding-left: 0.5em;
    font-size: 3em;
}
.subtitulos{
    display: flex;
    margin-left: 1em;
    margin-right: 4em;
    margin-top: 1em;
}
.right{
    margin-left: auto;
    order: 2;
}
</style>