import Vue from 'vue'
import Vuex from 'vuex'
import moment from 'moment'
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

Vue.filter('formatDate', function (value) {
  if (value) {
    return moment(String(value)).format('MM/DD/YYYY')
  }
})

Vue.filter('capitalize', (value) => {
  if (value) {
    return value.charAt(0).toUpperCase() + value.slice(1).toLowerCase()
  }
})

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
