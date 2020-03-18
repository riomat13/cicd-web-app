import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    access: localStorage.getItem('at') || '',
    refresh: localStorage.getItem('rt') || '',
    isAuthenticated: localStorage.getItem('username') !== null
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
            localStorage.setItem('at', access)
            localStorage.setItem('rt', refresh)
            commit('auth_success', access, refresh)
            localStorage.setItem('username', data.username)
            resolve(response)
          })
          .catch((err) => {
            commit('auth_failed')
            localStorage.removeItem('at')
            localStorage.removeItem('rt')
            localStorage.removeItem('username')
            reject(err)
          })
      })
    },
    logout: ({ commit }) => {
      return new Promise((resolve, reject) => {
        localStorage.removeItem('at')
        localStorage.removeItem('rt')
        localStorage.removeItem('username')
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
