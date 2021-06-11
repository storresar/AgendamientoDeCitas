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

    <div>
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
        <tr v-for="usuarioL in paginated" :key="usuarioL.id">
          <td>{{ usuarioL.id }}</td>
          <td>{{ usuarioL.first_name }} {{ usuarioL.last_name }}</td>
          <td>{{ usuarioL.email }}</td>
          <td>{{ usuarioL.username }}</td>
          <td>{{ usuarioL.fecha_nacimiento }}</td>
          <td>{{ mostrarRol(usuarioL.rol) }}</td>
          <td>{{ usuarioL.activo }}</td>
        </tr>
        <tfoot>
          <tr>
            <td></td>
            <td class="excel">
              <JsonExcel :data="JSON.parse(JSON.stringify(this.filtrarPorActivo))">
                <button>
                  <i class="fa fa-file-excel-o" aria-hidden="true"></i>
                </button>
              </JsonExcel>
            </td>
            <td class="pdf">
              <button @click="generarPDF()">
                <i class="fa fa-file-pdf-o" aria-hidden="true"></i>
              </button>
            </td>
            <td>
            </td>
            <td>              
            </td>
            <td>
              <button @click="restarPaginacion()" id="anterior"><<<<</button>
            </td>
            <td>
              <button @click="sumarPainacion()" id="siguiente">>>>></button>
            </td>
          </tr>
        </tfoot>
      </table>
    </div>
    
  </div>
</template>

<script>
import { mapState } from "vuex";
import JsonExcel from "vue-json-excel";
import jsPDF from 'jspdf'
import 'jspdf-autotable'
import logoImagen from '../store/logo'

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
      return this.filtrarPorActivo.slice(this.indexStart, this.indexEnd);
    },
    filtrarPorUsuario() {
      var lista = this.listaUsuarios;
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
        return lista;
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
      const usuarios = []
      this.filtrarPorActivo.forEach(obj => {
        usuarios.push([
            obj.id,
            `${obj.first_name} ${obj.last_name}`,
            obj.email,
            obj.username,
            obj.fecha_nacimiento,
            obj.rol===1?'Paciente':obj.rol===2?'Funcionario':'Admin',
            obj.activo?'Activo':'Inactivo']
          )
      });
      const doc = new jsPDF()
      doc.addImage(logoImagen, 'JPEG', 130, 0, 70, 50)
      const fecha = new Date().toISOString().slice(0,10)
      const time = new Date().toLocaleTimeString('en-US', {hour:'numeric', hour12:true, minute:'numeric'})
      doc.setFontSize(12)
      doc.text(10,25, `Usuario: ${this.usuario.username}`)
      doc.text(10,30, `Fecha: ${fecha} | ${time}`)
      doc.text(10,290, `Tipo Usuario: ${this.buscar===''?'todos':this.buscar} | estado: ${this.activo} | rol: ${this.tipo_usuario===1?'Paciente':this.tipo_usuario===2?'Funcionario':this.tipo_usuario===3?'Admin':'todos'}`)
      doc.autoTable({
        head: [['ID','Nombre', 'Email', 'Usuario', 'Fecha Nacimiento', 'Rol', 'Estado']],
        margin: {top:50, bottom:35},
        body: usuarios
      })
      const pdf = doc.output('blob')
      window.open(URL.createObjectURL(pdf))
    },
  },
};
</script>

<style scoped>
h1 {
  float: left;
  font-family: 'Lato', sans-serif; font-size: 35px; font-weight: 300; 
  margin-left: 1em;
  text-align: left;
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
.reporte tfoot tr{
  background-color: #063146;
  color: white;
}
.reporte tfoot tr {
  background-color: #063146;
  color: white;
}
.reporte tfoot tr {
  background-color: #063146;
  color: white;
}

#siguiente, #anterior{
  background-color: rgb(255, 255, 255);
  color: rgb(0, 0, 0);
  border: none;
  padding: 10px;
  border-radius: 6px;
  font-family: "Karla", sans-serif;
  font-size: 15px;
  width: 100px;
}
#siguiente:hover,#anterior:hover {
  background-color: gray;
  color: white;
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
.reporte tfoot tr{
  text-align: center;
  background-color: black;
  padding: 0;
}
.reporte tfoot tr:hover{
  background-color: black;
}
.excel button{
  width: 20%;
  height: 100%;
  border: none;
  background-color: #10bd52;
  color:white;
  font-size: 30px;
  border-radius:6px ;
}
.excel button:hover{
  background-color: #3bd677;
  cursor: pointer;
}
.pdf button{
  width: 20%;
  height: 100%;
  border: none;
  background-color: #bd1010;
  color:white;
  font-size: 30px;
  border-radius:6px ;
}
.pdf button:hover{
  background-color: #db3838;
  cursor: pointer;
}
</style>