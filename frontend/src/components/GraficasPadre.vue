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
            <div class="carta-info grafica">
                <CantidadTipoUsuarios/>
            </div>
        </div>
        <div class="grafica-fila2 hijo">
            <div class="carta-info grafica">
                <MujeresVsHombres/>
            </div>
            <div class="carta-info grafica">
                <ActivosVsInactivos/>
            </div>
            <div class="carta-info grafica">
                <RangoPorEdades/>
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
        ActivosVsInactivos : () => import('./Graficas/ActivosVsInactivos.vue'),
        RangoPorEdades : () => import('./Graficas/RangoDeEdades.vue')
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
    font-family: "Open Sans", sans-serif; 
    display: grid;
    grid-template-rows: 20vh 64vh 50vh;
    grid-template-columns: 100vw;
    grid-gap: 1em;
    background-color: black;
    overflow: auto;
    margin-right: 250px;
    color: white;
}
.hijo{
    background-color: black;
    margin: 1em;
    margin-right: 290px;
}
.grafica-fila1{
    display: grid;
    grid-gap: 2em; 
    grid-template-columns: 59% 38%;
    height: 80%;
}
.grafica-fila2{
    display: grid;
    column-gap: 1em; 
    grid-template-columns: 33% 31% 33%;
}
.info-general{
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    grid-gap: 1em;
}
.carta-info{
    background-color: #063146;
    text-align: left;
    border-radius: 1em;
}   
.carta-info p{
    margin: 0;
    margin-top: 1em;
    margin-left: 1em;
    padding: 0;
    font-size: 1em;
    font-weight: initial;
    color: #777b7e;
}
.carta-info .valor{
    padding-left: 0.5em;
    font-size: 3em;
}
.subtitulos{
    color: #777b7e;
    font-size: 0.9em;
    display: flex;
    margin-left: 1em;
    margin-right: 4em;
    margin-top: 1em;
}
.right{
    margin-left: auto;
    order: 2;
}

.grafica {
    padding-top: 1em;
    padding-bottom: 1em;
}

/* On screens that are 1440px wide or less, make the columns stack on top of each other instead of next to each other */
@media screen and (min-width: 1440px) {
    .componente{
      grid-template-rows: 15vh 45vh 50vh;
      grid-template-columns: 95vw;
    }
    .grafica-fila1{
        grid-template-columns: 59.7% 38%;
    }
    .grafica-fila2{
        grid-template-columns: 33% 31.5% 33%;
    }
}
</style>