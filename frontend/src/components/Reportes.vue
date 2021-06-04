<template>
  <div class="reporte">
    <h1 id = "titulo-reporte">REPORTE</h1>
    <div class="filtros">
      <input type="text" placeholder="Buscar Por Usuario" v-model="buscar" />
      <select v-model="tipo_usuario">
        <option value="1">PACIENTE</option>
        <option value="2">FUNCIONARIO</option>
        <option value="3">ADMINISTRADOR</option>
        <option value="todos">TODOS</option>
      </select>
      <select v-model="activo">
        <option value="activo">ACTIVO</option>
        <option value="inactivo">INACTIVO</option>
        <option value="todos">TODOS</option>
      </select>
    </div>

    <div id="reporte">
      <h1 id="reporte-titulo" style="display:none; position:fixed; top:20px; left:2em;">REPORTE</h1>
      <p id="reporte-info" style="clear: both; text-align:left; margin:1em; font-size:2em; display:none">
        Este reporte fue generado por el usuario {{usuario.username}} el dia {{tiempoReal}}
      </p>
      <table style="margin-top:1em">
        <thead>
          <th>ID</th>
          <th>NOMBRE</th>
          <th>EMAIL</th>
          <th>USUARIO</th>
          <th>FECHA NACIMIENTO</th>
          <th>ROL</th>
          <th>ACTIVO</th>
        </thead>
        <tr v-for="usuarioL in filtrarPorActivo" :key="usuarioL.id">
          <td>{{ usuarioL.id }}</td>
          <td>{{ usuarioL.first_name }} {{ usuarioL.last_name }}</td>
          <td>{{ usuarioL.email }}</td>
          <td>{{ usuarioL.username }}</td>
          <td>{{ usuarioL.fecha_nacimiento }}</td>
          <td>{{ mostrarRol(usuarioL.rol) }}</td>
          <td>{{ usuarioL.activo }}</td>
        </tr>
        <tr v-for="usuarioL in listaUsuarios" :key="usuarioL.email" style="display:none">
          <td>{{ usuarioL.id }}</td>
          <td>{{ usuarioL.first_name }} {{ usuarioL.last_name }}</td>
          <td>{{ usuarioL.email }}</td>
          <td>{{ usuarioL.username }}</td>
          <td>{{ usuarioL.fecha_nacimiento }}</td>
          <td>{{ mostrarRol(usuarioL.rol) }}</td>
          <td>{{ usuarioL.activo }}</td>
        </tr>
      </table>
    </div>
      
    <div id="paginacion">
      <ul>
        <button @click="restarPaginacion()" id="anterior">Anterior</button>
        <button @click="sumarPainacion()" id="siguiente">Siguiente</button>
      </ul>
    </div>
    <button @click="generarPDF()">Generar PDF</button>
    <JsonExcel :data="JSON.parse(JSON.stringify(this.filtrarPorActivo))">
      <button>
          Reporte excel
      </button>
    </JsonExcel>
  </div>
</template>

<script>
import { mapState } from "vuex";
import JsonExcel from "vue-json-excel";
import html2canvas from "html2canvas";
import pdfMake from "pdfmake/build/pdfmake";
import pdfFonts from "pdfmake/build/vfs_fonts";
pdfMake.vfs = pdfFonts.pdfMake.vfs;

export default {
  data() {
    return {
      nPaginacion: 7,
      nActual: 0,
      buscar: "",
      tipo_usuario: "todos",
      activo: "todos",
    };
  },
  components: {
    JsonExcel,
  },
  computed: {
    ...mapState(["listaUsuarios", 'usuario']),
    indexStart() {
      return this.nActual * this.nPaginacion;
    },
    indexEnd() {
      return this.indexStart + this.nPaginacion;
    },
    paginated() {
      return this.listaUsuarios.slice(this.indexStart, this.indexEnd);
    },
    filtrarPorUsuario() {
      var lista = this.paginated;
      if (this.buscar == "") {
        return lista;
      } else {
        return lista.filter((objeto) =>
          objeto.username.toLowerCase().includes(this.buscar.toLowerCase())
        );
      }
    },
    filtrarPorTipo() {
      var lista = this.filtrarPorUsuario;
      if (this.tipo_usuario == "todos") {
        return lista;
      } else {
        return lista.filter((objeto) => objeto.rol == this.tipo_usuario);
      }
    },
    filtrarPorActivo() {
      var lista = this.filtrarPorTipo;
      if (this.activo == "todos") {
        return lista.slice(this.indexStart, this.indexEnd);
      } else {
        if (this.activo == "activo") {
          return lista.filter((objeto) => objeto.activo == true);
        } else {
          return lista.filter((objeto) => objeto.activo == false);
        }
      }
    },
    tiempoReal(){
      return new Date().toISOString().slice(0,10) + ' a las ' + new Date().toLocaleTimeString('en-US', {hour:'numeric', hour12:true, minute:'numeric'})
    }
  },
  methods: {
    restarPaginacion() {
      if (this.nActual > 0) {
        this.nActual--;
      }
    },
    sumarPainacion() {
      if (
        this.nActual * this.nPaginacion + this.nPaginacion <
        this.listaUsuarios.length
      ) {
        this.nActual++;
      }
    },
    mostrarRol(rol) {
      if (rol == 1) {
        return "PACIENTE";
      } else if (rol == 2) {
        return "FUNCIONARIO";
      } else {
        return "ADMIN";
      }
    },
    generarPDF() {
      const reporte = document.querySelector('#reporte')
      reporte.children[0].style.display = 'block'
      reporte.children[1].style.display = 'block'
      console.log(reporte.children[2])
      for (let i = 1; i < this.nPaginacion+1; i++) {
        reporte.children[2].children[i].style.display = 'none'
        
      }
      for (let i = this.nPaginacion+1; i <= this.nPaginacion+ this.listaUsuarios.length; i++) {
        reporte.children[2].children[i].style.display = ''
        
      }
      console.log(reporte.children[2])
      html2canvas(reporte).then((canvas) => {
        var data = canvas.toDataURL()
        var docDefinition = {
          pageOrientation: "landscape",
          content: [
            {
              image: data,
              width: 950,
            },
          ],
        };
        pdfMake.createPdf(docDefinition).open();
        reporte.children[0].style.display = 'none'
        reporte.children[1].style.display = 'none'
        for (let i = 1; i <= this.nPaginacion; i++) {
          reporte.children[2].children[i].style.display = ''
        
        }
        for (let i = this.nPaginacion+1; i <= this.nPaginacion+ this.listaUsuarios.length; i++) {
          reporte.children[2].children[i].style.display = 'none'
        
        }
      })
    },
  },
  watch: {
    pdfReporte (val){
      if (val){
        this.generarPDF()
      }
    }
  }
};
</script>

<style scoped>
h1 {
  float: left;
  margin-left: 1em;
  font-size: 40px;
}
#reporte{
  height: 80vh;
}
.reporte table {
  width: 80%;
  background-color: white;
  text-align: left;
  color: black;
  top: 17%;
  left: 11px;
  border-collapse: collapse;
  position: fixed;
}
.reporte th, td {
  padding: 15px;
}
.reporte thead {
  background-color: #063146;
  color: white;
  border-bottom: solid 5px black;
}
.reporte tr:nth-child(even) {
  background-color: #ddd;
}
.reporte tr:hover {
  background-color: #063146;
  color: white;
}
#paginacion #anterior {
  position: fixed;
  top: 90%;
  left: 30%;
}

#paginacion #siguiente {
  position: fixed;
  top: 90%;
  left: 40%;
}
#paginacion button:hover {
  background-color: gray;
  color: white;
}
#paginacion button {
  background-color: black;
  color: white;
  border: none;
  padding: 10px;
  border-radius: 6px;
  font-family: "Karla", sans-serif;
  font-size: 15px;
  width: 100px;
}
.reporte .filtros {
  float: left;
  margin-left: 2em;
  margin-top: 2em;
  display: inline-block;
}
.reporte input {
  margin-left: 3em;
  width: 200px;
  height: 30px;
  background: white;
  border: none;
  font-size: 10pt;
  float: left;
  color: black;
  padding-left: 45px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;
  border: black solid 3px;
}
.reporte select {
  margin-left: 2em;
  width: 200px;
  height: 38px;
  background: white;
  border: none;
  font-size: 10pt;
  float: left;
  color: black;
  padding-left: 45px;
  -webkit-border-radius: 5px;
  -moz-border-radius: 5px;
  border-radius: 5px;
  border: black solid 3px;
}
</style>