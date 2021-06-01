<script>
import { Bar } from "vue-chartjs";
import { mapState } from 'vuex'

export default {
    
    extends: Bar,
    data(){
        return{
            cActivos: 0,
            cInactivos: 0
        }
    },
    computed: {
    ...mapState(['listaUsuarios']),
    },
    methods:{
        calcularCantidades(){
            for (let i = 0; i < this.listaUsuarios.length; i++) {
                if(this.listaUsuarios[i].activo == true){
                    this.cActivos++
                }else{
                    this.cInactivos++
                }
            }
        }
    },
    mounted() {
        this.calcularCantidades()
        this.renderChart(
            {
                labels: [
                "Activos",
                "Inactivos",
                ],
                datasets: [
                {
                    label: "ACTIVOS VS INACTIVOS",
                    backgroundColor: "#f87979",
                    data: [this.cActivos,this.cInactivos]
                }
                ]
            },
            { responsive: true, maintainAspectRatio: false }
            );
    }
    };
</script>