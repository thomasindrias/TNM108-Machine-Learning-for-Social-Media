import 'bootstrap/dist/css/bootstrap.css';
import 'animate.css';
import VueScrollReveal from 'vue-scroll-reveal';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import Vue from 'vue';
import bootstrapvue from 'bootstrap-vue';
import App from './App.vue';
import router from './router';

Vue.use(VueScrollReveal, {
  duration: 400,
  scale: 1,
  distance: '30px',
  reset: true,
  mobile: false,
});
Vue.use(bootstrapvue);

Vue.config.productionTip = false;

new Vue({
  router,
  render: h => h(App),
}).$mount('#app');
