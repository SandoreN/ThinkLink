
import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store';
import './style.css';
import LottieVuePlayer from '@lottiefiles/vue-lottie-player'

Vue.use(LottieVuePlayer)
Vue.config.productionTip = false

new Vue({
  render: h => h(App),
  router,
  store
}).$mount('#app')