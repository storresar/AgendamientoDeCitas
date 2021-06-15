<template>
    <div class="container">
        <section class="form_registro">
            <h4>Recuperación cuenta</h4>
            <input class="control" type="password" placeholder="Ingrese su nueva clave" v-model.trim="$v.clave.$model" autocomplete="off">
            <div class="error" v-if="!$v.clave.minLength">Su clave debe contener al menos 8 caracteres y uno de ellos numerico</div>
            <input class="control" type="password" placeholder="Confirme su clave" v-model.trim="$v.repita.$model" autocomplete="off">
            <div class="error" v-if="!$v.repita.sameAsClave">Las contraseñas no coinciden</div>
            <div class="submit">
                <button class="boton" @click="reactivarUsuario()">Recuperar clave</button>
            </div>
        </section>
    </div>
</template>

<script>

import { required, minLength, sameAs } from 'vuelidate/lib/validators'
import { esFuerte } from '../validators/validator'
import { mapState } from 'vuex'

export default {
    data(){
        return {
            token: this.$route.params.token,
            usuario: this.$route.params.nom_usuario,
            clave: '',
            repita: '',
        }
    },
    validations(){
        return {
            clave:{
                required,
                minLength: minLength(8),
                esFuerte,
            },
            repita: {
                required,
                sameAsClave: sameAs('clave')
            },
        }
    },
    computed:{
        ...mapState(['url'])
    },
    methods: {
        reactivarUsuario(){
            this.$v.$touch()
            if (this.$v.$invalid){
                this.$alert('Llene los datos adecuadamente','Error en el formulario','warning')
            } else  {
                fetch(`${this.url}reactivar_usuario/` , {
                    method : 'POST',
                    headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${this.token}`
                    },
                    body: JSON.stringify({
                        username: this.usuario,
                        clave: this.clave,
                        confirma : this.repita
                    })
                })
                .then(res => {
                    if (res.ok) {
                        this.$alert('Su cuenta fue restaurada exitosamente','Exito','success')
                        this.$router.push('/login')
                    } else {
                        this.$alert('Fallo en el servidor, intentelo nuevamente mas tarde','Error','error')
                        this.$router.push('/')
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
    color: red;
    font-size: 0.75em;
}
</style>