<template>
    <section class="form_registro">
        <h4>¡ BIENVENIDO !</h4>
        <h4>Ingresar</h4>
        <input class="control" type="text" placeholder="Ingrese su usuario" v-model="nombre" autocomplete="off">
        <input class="control" type="password"  placeholder="Ingrese su contraseña" v-model="clave" autocomplete="off" id="clave">
        Mostrar Contraseña
        <input type="checkbox" id="cbox2" value="checkbox" v-model="check">
        <VueRecaptcha class="captcha"
        sitekey="6LdY2egaAAAAAInX0sJZ8urUHpBWb9isu9arAqP_"
        :loadRecaptchaScript="true"
        @verify="onVerify"
        @expired="verificado=false"
        theme="Dark">
        </VueRecaptcha>
        <button class="boton" @click="mandarDatos()">Ingresar</button>
        <router-link to="/recuperar_cuenta">Desbloquee su cuenta aqui</router-link>
    </section>
</template>

<script>
import { mapActions, mapState } from 'vuex'
import VueRecaptcha from 'vue-recaptcha';

export default {
    data(){
        return {
            nombre: 'admin',
            clave: 'Santi123',
            check: false,
            verificado: false,
        }
    },
    components:{
        VueRecaptcha,
    },
    computed: {
        ...mapState(['url'])
    },
    methods:{
        ...mapActions(['autenticar']),
        mandarDatos(){
            const datos = {username:this.nombre, password:this.clave}
            if (this.verificado){
                this.autenticar(datos)
                .then(() => this.$router.push('/admin')) 
                .catch(msg => this.$alert(msg,'Error','warning'))
            } else{
                this.reloadCaptcha()
            }
        },
        onVerify(response) {
            fetch(`${this.url}/verificar_captcha/`,{
                method:'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    'g-recaptcha-response': response
                }),
            }).then(req => req.json())
            .then(res => res? this.verificado=true: reloadCaptcha())
            .catch(() => this.$alert('Error de servidor. Intentalo mas tarde','Ha ocurrido un error','error'))
        },
        reloadCaptcha(){
            grecaptcha.reset()
            this.$alert('Reintente la verificacion','Fallo en el captcha','error')
        }
    },
    watch:{
            check: function(antiguo){
                var tipo = document.getElementById("clave");
                if(antiguo) {
                    tipo.type = "text";
                }else{
                    tipo.type = "password";
            }
    },
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

.captcha{
    margin-left: 3em;
    margin-top: 1em;
}
</style>