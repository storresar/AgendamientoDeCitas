<script>
import { Bar } from "vue-chartjs";
import { mapState, mapActions } from 'vuex'

export default {
    
    extends: Bar,
    data(){
        return{
            cMujeres: 0,
            cHombres: 0,
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
    ...mapState(['listaUsuarios','paciente']),
    },
    methods:{
            ...mapActions(['getPaciente']),
        async calcularCantidades(){
            for (let i = 0; i < this.listaUsuarios.length; i++) {
                if(this.listaUsuarios[i].rol == 1){
                    await this.getPaciente(this.listaUsuarios[i].id)
                    if(this.paciente.sexo == 'M'){
                        this.cHombres++
                    }else{
                        this.cMujeres++
                    }
                }
            }
        }
    },
    mounted() {
        this.calcularCantidades().then(() => {
            this.renderChart(
            {
                labels: [
                "Hombres",
                "Mujeres",
                ],
                datasets: [
                {
                    label: "HOMBRES VS MUJERES",
                    backgroundColor: "#7F38D0",
                    color: "white",
                    data: [this.cHombres,this.cMujeres]
                }
                ]
            },
            this.options
            );
        })
    },
    };
</script>