import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import store from './store';
import './style.css';
//import LottieVuePlayer from '@lottiefiles/vue-lottie-player';
import axios from 'axios';

axios.defaults.withCredentials = true;

const app = createApp(App);

app.use(router);
app.use(store);
//app.use(LottieVuePlayer);

app.mount('#app');