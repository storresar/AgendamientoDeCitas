<template>
  <div class="home">
    <nav class="menu-main">
		<router-link to="/registro"> Registrarse</router-link>
		<router-link to="/login">Pagina Login</router-link>
	</nav>
	<nav class="menu-main">
		<a href="#">PERSONA <br> Afiliación y Servicio</a>
		<a href="#">SALUD <br> EPS y Plan Complementario</a>
		<a href="#">SOBRE SOPHY HOSPITAL <br> Información Institucional</a>
	</nav>
	<div class="slider">
		<ul>
			<li><img src="../assets/1.jpg" alt=""></li>
			<li><img src="../assets/2.jpg" alt=""></li>
			<li><img src="../assets/3.jpg" alt=""></li>
		</ul>
	</div>
	<div class="section">
		<div class="box">
			<img src="../assets/vacunación.jpg" alt="">
			<div class="hover">
				<h1>Vacunación</h1>
			</div>
		</div>
		<div class="box">
			<img src="../assets/enfermedad.jpg" alt="">
			<div class="hover">
				<h1>Prevención de Enfermedades</h1>
			</div>
		</div>
		<div class="box">
			<img src="../assets/maternidad.jpg" alt="">
			<div class="hover">
				<h1>Maternidad</h1>
			</div>
		</div>
	</div>
  </div>
</template>


<style scoped>
.slider{
	width: 70%;
	margin: auto;
	overflow: hidden;
}

.slider ul{
	display: flex;
	padding: 0;
	width: 300%;
	animation: cambio 20s infinite;
}

.slider li{
	width: 100%;
	list-style: none;
}

.slider img{
	width: 100%;
}

@keyframes cambio{
	0% {margin-left: 0;}
	25% {margin-left: 0;}
	30% {margin-left: -100%;}
	55% {margin-left: -100%;}
	80% {margin-left: -200%;}
	100% {margin-left: -200%;}
}

body{
	margin: 0px;
	background-color: aliceblue;
}

.menu-main{
	display: flex;
	justify-content: space-between;
	background: #3b5998;
	border-bottom: 1px solid #29487d;
	height: 45px;
}

.menu-main a{
	flex: 1;
	font-family: arial;
	display: flex;
	color: #ffffff;
	text-decoration: none;
	font-size: 12px;
	font-weight: bold;    
	justify-content: center;
	align-items: center;
}

.menu-main a:hover{
	background: rgba(0,0,0, .1);
}

.menu-main a.active{
	background-color: #29487d;
}

@media (max-width: 768px) {

	.menu-main{
		height: auto;
		border-bottom: 0px;
		display: block;
	}

	.menu-main a{
		height: 45px;
		border-bottom: 1px solid #29487d;
	}

}
.section{
	width: 100%;
	height: 100vh;
	background-color: aliceblue;
	display: flex;
	justify-content: center;
	align-items: center;
}
.box{
	width: 30%;
	height: 50vh;
	text-align: hidden;
	position: relative;
	margin: 1.5%;
	border-image: 10px;
}

.box img{
	width: 100%;
	height:100%;
	object-fit: cover;
}

.box .hover{
	width: 0;
	height: 50vh;
	background-color: rgba(56,53,53,0.568);
	position: absolute;
	top: 0;
	display: flex;
	justify-content: center;
	align-items: center;
	overflow: hidden;
	transition: .4s all;
}
.hover h1{
	color: aliceblue;
	text-shadow: 1px 1px 1px black;
	font-size: 2.5em;
	text-transform: uppercase;
}
.box:hover .hover{
	width: 100%
}

</style>

<script>
export default {
  name: 'Home',
  components: {
  }
}
</script>
