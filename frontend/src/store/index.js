import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    access: sessionStorage.getItem('at') || '',
    refresh: sessionStorage.getItem('rt') || '',
    isAuthenticated: sessionStorage.getItem('username') !== null
  },
  mutations: {
    auth_request (state) {
      state.status = 'loading'
    },
    auth_success (state, access, refresh) {
      state.status = 'success'
      state.isAuthenticated = true
    },
    auth_failed (state) {
      state.status = 'error'
    },
    let_logout (state) {
      state.status = ''
      state.isAuthenticated = false
    }
  },
  actions: {
    login: ({ commit }, data) => {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        Vue.prototype.$http.post('/api/account/login/token/',
          {
            username: data.username,
            password: data.password
          })
          .then((response) => {
            const access = response.data.access
            const refresh = response.data.refresh
            Vue.prototype.$http.defaults.headers.common.Authorization = access
            sessionStorage.setItem('at', access)
            sessionStorage.setItem('rt', refresh)
            commit('auth_success', access, refresh)
            sessionStorage.setItem('username', data.username)
            resolve(response)
          })
          .catch((err) => {
            commit('auth_failed')
            sessionStorage.removeItem('at')
            sessionStorage.removeItem('rt')
            sessionStorage.removeItem('username')
            reject(err)
          })
      })
    },
    logout: ({ commit }) => {
      return new Promise((resolve, reject) => {
        sessionStorage.removeItem('at')
        sessionStorage.removeItem('rt')
        sessionStorage.removeItem('username')
        delete Vue.prototype.$http.defaults.headers.common.Authorization
        commit('let_logout')
        resolve()
      })
    }
  },
  modules: {
  },
  getters: {
    isLoggedIn: state => !!state.isAuthenticated
  }
})
