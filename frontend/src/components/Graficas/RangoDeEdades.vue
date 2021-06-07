<script>
import { Bar } from "vue-chartjs";
import { mapState } from 'vuex'

export default {
    
    extends: Bar,
    data(){
        return{
            cNinos: 0,
            cJovenes: 0,
            cAdultos:0,
            cAncianos:0
        }
    },
    computed: {
    ...mapState(['listaUsuarios']),
    },
    methods:{
        calcularCantidades(){
            for (let i = 0; i < this.listaUsuarios.length; i++) {
                let edad = this.calcularEdad(this.listaUsuarios[i].fecha_nacimiento)
                if(edad <= 12){
                    this.cNinos++
                }else if(edad <= 24){
                    this.cJovenes++
                }else if(edad <= 59){
                    this.cAdultos++
                }else{
                    this.cAncianos++
                }
            }
        },
        calcularEdad(fecha) {
            var hoy = new Date();
            var cumpleanos = new Date(fecha);
            var edad = hoy.getFullYear() - cumpleanos.getFullYear();
            var m = hoy.getMonth() - cumpleanos.getMonth();

            if (m < 0 || (m === 0 && hoy.getDate() < cumpleanos.getDate())) {
                edad--;
            }

            return edad;
        }
    },
    mounted() {
        this.calcularCantidades()
        this.renderChart(
            {
                labels: [
                "Niños",
                "Jovenes",
                "Adultos",
                "Ancianos"
                ],
                datasets: [
                {
                    label: "POR EDADDES",
                    backgroundColor: ["#FFF","#7000DF", "#13C5E2", "#FE3F6F"],
                    data: [this.cNinos,this.cJovenes,this.cAdultos,this.cAncianos]
                }
                ]
            },
            { responsive: true, maintainAspectRatio: false }
            );
    }
    };
</script>