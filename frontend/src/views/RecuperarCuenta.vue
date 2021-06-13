<template>
    <div class="container">
        <section class="form_registro">
            <h4>Recuperación cuenta</h4>
            <input class="control" type="email" placeholder="Ingrese el correo registrado a su cuenta" v-model.trim="$v.correo.$model" autocomplete="off">
            <div class="error" v-if="!$v.correo.email">Correo Invalido</div>
            <div class="submit">
                <button class="boton" @click="mandarCorreo()">Recuperar cuenta</button>
            </div>
        </section>
    </div>
</template>

<script>

import { required, email } from 'vuelidate/lib/validators'

export default {
    data(){
        return {
            correo: ''
        }
    },
    validations(){
        return {
            correo:{
                required,
                email
            },
        }
    },
    methods: {
        mandarCorreo(){
            this.$v.$touch()
            if (this.$v.$invalid){
                this.$alert('Llene los datos adecuadamente','Error en el formulario','warning')
            } else  {
                fetch(`http://127.0.0.1:8000/api/mandar_correo/` , {
                    method : 'POST',
                    headers: {
                    'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        email: this.correo,
                    })
                })
                .then(res => {
                    if (res.ok) {
                        this.$alert('Se ha enviado unas instrucciones a su correo. Reviselas por favor','Exito','success')
                        this.$router.push('/')
                    } else {
                        res.json()
                        .then((msg) => this.$alert(msg,'Fallo','error'))
                    }
                })
                .catch(() => {
                    this.$alert('Fallo en el servidor, intentelo nuevamente mas tarde','Error','error')
                    this.$router.push('/')
                })
            }
        }
    }
}
</script>


<style scoped>



.form_registro{
    width: 400px;
    background: #042331;
    padding: 20px;
    margin: auto;
    margin-top: 3em;
    font-family: 'Poppins', sans-serif;
    color: white;
}
.form_registro h4{
    font-size: 25px;
    margin-bottom: 30px;
    text-align: center;
    color: white;
}
.control{
    font-family: inherit;
    width: 100%;
    border: 0;
    border-bottom: 2px solid gray;
    outline: 0;
    font-size: 1.0rem;
    color: white;
    padding: 7px 0;
    background: transparent;
    transition: border-color 0.2s;
    margin-bottom: 25px;
    margin-top: 25px;
}
.control:focus{
    font-family: inherit;
    width: 100%;
    border: 0;
    border-bottom: 2px solid #43e9db;
    outline: 0;
    font-size: 1.0rem;
    color: rgb(245, 234, 234);
    padding: 7px 0;
    background: transparent;
    transition: border-color 0.2s;
    margin-bottom: 25px;
}

.form_registro p{

    height: 40px;
    text-align: center;
    font-size: 14px;
}
.form_registro a{
    color: white;
    text-decoration: none;
}
.form_registro i{
    background: white;
    font-size: 22px;
}
.form_registro a:hover{
    color: whitesmoke   ;
    text-decoration: underline;
}
.form_registro .boton {
    width: 100%;
    background: gray;
    border: none;
    padding: 20px;
    color: white;
    margin: 20px 0;
    font-size: 12px;
    border-radius: 1px;
}

.error{
    color: rgb(187, 36, 36);
    font-size: 0.75em;
}
</style>