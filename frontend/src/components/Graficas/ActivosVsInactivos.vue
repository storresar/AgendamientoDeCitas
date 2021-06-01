<script>
import { Bar } from "vue-chartjs";
import { mapState } from 'vuex'

export default {
    
    extends: Bar,
    data(){
        return{
            cActivos: 0,
            cInactivos: 0,
            options: {
                scales: {
                    yAxes: [{
                    stacked: true,
                    ticks: {
                        beginAtZero: true,
                        min: 0,
                    },
                    }],
                    xAxes: [{
                    stacked: true,
                    ticks: {
                        beginAtZero: true,
                        categoryPercentage: 0.5,
                        barPercentage: 1,
                    },
                    }],
                },
                responsive: true,
                maintainAspectRatio: false,
            },
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
            this.options
            );
    }
    };
</script>