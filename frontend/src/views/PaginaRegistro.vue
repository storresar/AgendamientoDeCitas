<template>
  <div>
    <div id="wrapper">
      <h1>Formulario de Registro</h1>
      <form onsubmit="return false">
        <div class="col-2">
          <label>
            Nombre
            <input
              placeholder="Ingrese su Nombre Completo"
              id="name1"
              name="name1"
              tabindex="1"
            />
          </label>
        </div>
        <div class="col-2">
          <label>
            Apellido
            <input
              placeholder="Ingrese su Apellido Completo"
              id="name2"
              name="name2"
              tabindex="2"
            />
          </label>
        </div>
        <div class="col-2">
          <label>
            Edad
            <input
              placeholder="Ingrese su Edad"
              id="age"
              name="age"
              tabindex="3"
            />
          </label>
        </div>
        <div class="col-3">
          <label>
            Correo Electrónico
            <input
              placeholder="Ingrese su correo electrónico"
              id="email"
              name="email"
              tabindex="4"
            />
          </label>
        </div>
        <div class="col-3">
          <label>
            RH
            <input
              placeholder="Seleccione su tipo de sangre"
              id="rh"
              name="rh"
              tabindex="5"
            />
          </label>
        </div>
        <div class="col-3">
          <label>
            Sexo
            <input
              placeholder="Seleccione su sexo"
              id="gender"
              name="gender"
              tabindex="6"
            />
          </label>
        </div>
        <div class="col-3">
          <label>
            Tipo de Documento
            <input
              placeholder="Seleccione su tipo de documento"
              id="document"
              name="document"
              tabindex="7"
            />
          </label>
        </div>
        <div class="col-4">
          <label>
            Número de Documento
            <input
              placeholder="Ingrese su número de documento"
              id="documentnumber"
              name="documentnumber"
              tabindex="8"
            />
          </label>
        </div>
        <div class="col-4">
          <label>
            Usuario
            <input
              placeholder="Ingrese un nombre de Usuario"
              id="user"
              name="user"
              tabindex="9"
            />
          </label>
        </div>
        <div class="col-4">
          <label>
            Contraseña
            <input
              placeholder="Ingrese una ncontraseña"
              id="password"
              name="pasword"
              tabindex=""
            />
          </label>
        </div>

        <div class="col-submit">
          <button class="submitbtn">Registrarse</button>
        </div>
      </form>
    </div>
  </div>
</template>

<style scoped>
@import url(http://fonts.googleapis.com/css?family=Laila:400,700);

html {
  overflow-y: scroll;
}
body {
  font-family: Arial, Tahoma, sans-serif;
  background: #e2eef4;
  font-size: 62.5%;
  line-height: 1;
  padding-top: 40px;
}

br {
  display: block;
  line-height: 1.6em;
}

input,
textarea {
  -webkit-font-smoothing: antialiased;
  outline: none;
}

strong,
b {
  font-weight: bold;
}
em,
i {
  font-style: italic;
}

h1 {
  display: block;
  font-size: 3.1em;
  line-height: 1.45em;
  font-family: "Laila", serif;
  text-align: center;
  font-weight: bold;
  color: #555;
  text-shadow: 1px 1px 0 #fff;  
}

/** form field **/
form {
  display: block;
  margin: 30px;
  overflow: hidden;
  background: #fff;
  border: 1px solid #e4e4e4;
  border-radius: 5px;
  font-size: 0;
}

form > div > label {
  display: block;
  padding: 20px 20px 10px;
  vertical-align: top;
  font-size: 13px;
  font-weight: bold;
  text-transform: uppercase;
  color: #939393;
  cursor: pointer;
}
form > div.switch > label {
  padding: 16px 20px 13px;
}

.col-2,
.col-3,
.col-4 {
  border-bottom: 1px solid #e4e4e4;
}

form > div > .col-4 {
  height: 86px;
}

label > input {
  display: inline-block;
  position: relative;
  width: 100%;
  height: 27px;
  line-height: 27px;
  margin: 5px -5px 0;
  padding: 7px 5px 3px;
  border: none;
  outline: none;
  color: #555;
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-weight: bold;
  font-size: 14px;
  opacity: 0.6;
  transition: all linear 0.3s;
}

.col-submit {
  text-align: center;
  padding: 20px;
}

label > select {
  display: block;
  width: 100%;
  padding: 0;
  color: #555;
  margin: 16px 0 6px;
  font-weight: 500;
  background: transparent;
  border: none;
  outline: none;
  font-family: "Helvetica Neue", Arial, sans-serif;
  font-size: 14px;
  opacity: 0.4;
  transition: all linear 0.3s;
}

label > input:focus,
label > select:focus {
  opacity: 1;
}

/** button design based on http://codepen.io/guvootes/pen/eyDAb **/
button {
  width: 100%;
  height: 35px;
  border: none;
  border-radius: 4px;
  margin: 0 0 15px 0;
  font-size: 14px;
  color: #fff;
  font-weight: bold;
  text-shadow: 1px 1px 0 rgba(0, 0, 0, 0.3);
  overflow: hidden;
  outline: none;
}

button.submitbtn {
  background-image: -moz-linear-gradient(#6b95c1, #599bb9);
  background-image: -webkit-linear-gradient(#6b95c1, #599bb9);
  background-image: linear-gradient(#6b95c1, #599bb9);
  border-bottom: 1px solid #3a738c;
  cursor: pointer;
  color: #fff;
}
button.submitbtn:hover {
  background-image: -moz-linear-gradient(#599bb9, #4a8aaf);
  background-image: -webkit-linear-gradient(#599bb9, #4a8aaf);
  background-image: linear-gradient(#599bb9, #4a8aaf);
}
button.submitbtn:active {
  height: 34px;
  border-bottom: 0;
  margin: 1px 0 0 0;
  background-image: -moz-linear-gradient(#4a8aaf, #599bb9);
  background-image: -webkit-linear-gradient(#4a8aaf, #599bb9);
  background-image: linear-gradient(#4a8aaf, #599bb9);
  -moz-box-shadow: inset 0 1px 3px 1px rgba(0, 0, 0, 0.3);
  -webkit-box-shadow: inset 0 1px 3px 1px rgba(0, 0, 0, 0.3);
  box-shadow: inset 0 1px 3px 1px rgba(0, 0, 0, 0.3);
}

/** responsive design **/
@media (min-width: 850px) {
  form > div {
    display: inline-block;
  }
  .col-submit {
    display: block;
  }

  .col-2,
  .col-3,
  .col-4 {
    box-shadow: 1px 1px #e4e4e4;
    border: none;
  }

  .col-2 {
    width: 50%;
  }
  .col-3 {
    width: 33.3333333333%;
  }
  .col-4 {
    width: 25%;
  }

  .col-submit button {
    width: 30%;
    margin: 0 auto;
  }
}
</style>