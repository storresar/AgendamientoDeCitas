<template>
    <h1>Bienvenido {{usuario.username}}</h1>
</template>
<script>
import { mapState } from 'vuex'
export default {
    computed:{
        ...mapState(['usuario'])
    }
}
</script>