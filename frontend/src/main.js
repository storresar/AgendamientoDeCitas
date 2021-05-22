import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import VueSimpleAlert from "vue-simple-alert";
import Vuelidate from 'vuelidate'

Vue.use(Vuelidate)
Vue.use(VueSimpleAlert);
Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
