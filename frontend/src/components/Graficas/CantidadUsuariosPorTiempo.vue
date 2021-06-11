<script>
import { Line } from "vue-chartjs";
import { mapState } from 'vuex'

export default {
    extends: Line,
    data() {
        return{
            meses:[
                'Enero',
                'Febrero',
                'Marzo',
                'Abril',
                'Mayo',
                'Junio',
                'Julio',
                'Agosto',
                'Septiembre',
                'Octubre',
                'Nobiemre',
                'Diciembre',
            ],
            fecha: new Date(),
            diasMes : 0,
            mes: 0,
            anio: 0,
        }
    },
    computed: {
        ...mapState(['listaUsuarios']),
        calcularUsuariosXMes(mes){}
    },
    mounted() {
        this.dia = this.fecha.getDay()
        this.anio = this.fecha.getYear()
        const mes = this.fecha.getMonth()
        this.diasMes = new Date(this.anio, mes +1, 0).getDate()
        const rangos = []
        const cant = []
        for (let i = 0; i <= this.diasMes; i++) {
            if (i%5 == 0){
                rangos.push(i + 1)
                cant.push(0)
            }
        }
        if (this.diasMes % 5 != 0){
            rangos.push(this.diasMes)
            cant.push(0)
        }
        const nuevo = rangos.map((rangodias) => new Date(this.anio+1900, mes, rangodias))
        this.listaUsuarios.map((obj) => {
            for (let i = 1; i < nuevo.length; i++) {
                const fUsu = new Date(obj.date_joined)
                if (fUsu >= nuevo[i-1] && nuevo[i] > fUsu){
                    cant[i]++
                }
            }
        })
        this.renderChart(
        {
            labels: rangos,
            datasets: [
            {
                label: "Usuarios registrados",
                data: cant,
                backgroundColor: "transparent",
                borderColor: "rgba(1, 116, 188, 0.50)",
                pointBackgroundColor: "rgba(171, 71, 188, 1)"
            }]
        },
        {
            responsive: true,
            maintainAspectRatio: false,
            title: {
            display: true,
            text: `Usuarios registrados el mes de ${this.meses[mes]}`
            }
        });
    }
};
</script>