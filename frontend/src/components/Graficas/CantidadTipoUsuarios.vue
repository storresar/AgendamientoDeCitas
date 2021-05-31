
<script>
import { Pie } from "vue-chartjs";
import { mapState } from 'vuex';

export default {
  name: 'CantidadTipoUsuarios',
  data() {
    return {
      cPacientes: 0,
      cFuncionarios: 0,
      cAdmins: 0,
    }
  },
  computed: {
    ...mapState(['listaUsuarios']),
  },
  methods: {
    calcularUsuarios(){
      for (let i = 0; i < this.listaUsuarios.length; i++) {
        if (this.listaUsuarios[i].rol === 1){
          this.cPacientes++
        }
        if (this.listaUsuarios[i].rol === 2){
          this.cFuncionarios++
        }
        if (this.listaUsuarios[i].rol === 3){
          this.cAdmins++
        }
      }
    }
  },

  extends: Pie,
  mounted() {
    this.calcularUsuarios()
    this.gradient = this.$refs.canvas
      .getContext("2d")
      .createLinearGradient(0, 0, 0, 450);
    this.gradient2 = this.$refs.canvas
      .getContext("2d")
      .createLinearGradient(0, 0, 0, 450);

    this.gradient.addColorStop(0, "rgba(255, 0,0, 0.5)");
    this.gradient.addColorStop(0.5, "rgba(255, 0, 0, 0.25)");
    this.gradient.addColorStop(1, "rgba(255, 0, 0, 0)");

    this.gradient2.addColorStop(0, "rgba(0, 231, 255, 0.9)");
    this.gradient2.addColorStop(0.5, "rgba(0, 231, 255, 0.25)");
    this.gradient2.addColorStop(1, "rgba(0, 231, 255, 0)");
    this.renderChart(
      {
        labels: ["Administradores", "Pacientes", "Funcionarios"],
        datasets: [
          {
            backgroundColor: [this.gradient, this.gradient2, "#00D8FF"],
            data: [this.cAdmins, this.cPacientes, this.cFuncionarios],
          },
        ],
      },
      { responsive: true, maintainAspectRatio: false }
    );
  },
};
</script>