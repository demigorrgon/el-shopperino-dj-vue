import Vue from 'vue'
import Vuex from 'vuex'
// import { verifyToken } from '@/api/shortcuts'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    accessToken: null,
    refreshToken: null,

  },
  getters: {
    isLoggedIn() {
      return localStorage.getItem('accessToken') !== null // check if valid on top of it
    }
  },
  mutations: {
    authorizeUser(state, user) {
      state.user = user;
    },
    setAccessToken(state, token) {
      // state.accessToken = token;
      localStorage.setItem('accessToken', token)
      state.accessToken = localStorage.getItem('accessToken')

    },
    setRefreshToken(state, token) {
      console.log(token)
      localStorage.setItem('refreshToken', token)
      state.refreshToken = localStorage.getItem('refreshToken')
    }
  },
  actions: {
    // initializeUser({ commit }) {
    //   try {
    //     let accessToken = localStorage.getItem('accessToken')
    //     console.log(verifyToken(accessToken))
    //     commit("authorizeUser", verifyToken(accessToken))
    //   }
    //   catch (error) {
    //     console.log(error)
    //   }
    // }
  },
  modules: {
  }
})
