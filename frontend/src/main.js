import Vue from 'vue'
import Vuex from 'vuex'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'

Vue.use(Vuex)

Vue.config.productionTip = false
Vue.prototype.$http =
  process.env.VUE_APP_REST_SERVER === 'mock-server'
    ? require('axios').create({ baseURL: 'http://localhost:3000' })
    : require('axios').create()

const token = localStorage.getItem('token')
if (token) {
  Vue.prototype.$http.defaults.headers.common.Authorization = token
}

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
