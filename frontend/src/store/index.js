import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user: ''
  },
  mutations: {
    auth_request (state) {
      state.status = 'loading'
    },
    auth_success (state, token, user) {
      state.status = 'success'
      state.token = token
      state.user = user
    },
    auth_failed (state) {
      state.status = 'error'
    },
    logout (state) {
      state.status = ''
      state.token = ''
      state.user = ''
    }
  },
  actions: {
    login: ({ commit }, username, password) => {
      return new Promise((resolve, reject) => {
        commit('auth_request')
        Vue.prototype.$http.post('/api/account/login',
          {
            username: username,
            password: password
          })
          .then((response) => {
            const token = response.data.token
            const user = response.data.user
            Vue.prototype.$http.defaults.headers.common.Authorization = token
            localStorage.setItem('token', token)
            commit('auth_success', token, user)
            resolve(response)
          })
          .catch((err) => {
            commit('auth_failed')
            localStorage.removeItem('token')
            reject(err)
          })
      })
    },
    logout: ({ commit }) => {
      return new Promise((resolve, reject) => {
        commit('logout')
        localStorage.removeItem('token')
        delete Vue.prototype.$http.defaults.headers.common.Authorization
        resolve()
      })
    }
  },
  modules: {
  },
  getters: {
    isLoggedIn: state => !!state.token,
    getAuthStatus: state => state.status
  }
})
