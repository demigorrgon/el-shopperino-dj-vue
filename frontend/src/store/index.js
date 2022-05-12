import Vue from 'vue'
import Vuex from 'vuex'
import { verifyToken, loadProductsResults } from '@/api/shortcuts'
import jwt_decode from 'jwt-decode'
import createPersistedState from 'vuex-persistedstate'
Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: null,
    accessToken: null,
    refreshToken: null,
    tokenValid: null,
    products: null,
    cart: [],

  },
  getters: {
    activeUser(state) {
      return state.user
    },
    tokenValid(state) {
      return state.tokenValid
    },
    itemsInCart(state) {
      return state.cart
    }
  },
  mutations: {
    authorizeUser(state) {
      const decodedToken = jwt_decode(localStorage.getItem('accessToken'))
      // check if valid on top of it
      state.user = decodedToken.username
    },
    setAccessToken(state, token) {
      // state.accessToken = token;
      localStorage.setItem('accessToken', token)
      state.accessToken = localStorage.getItem('accessToken')

    },
    setRefreshToken(state, token) {
      localStorage.setItem('refreshToken', token)
      state.refreshToken = localStorage.getItem('refreshToken')
    },
    isTokenValid(state, isValid) {
      state.tokenValid = isValid
    },
    logout(state) {
      localStorage.removeItem('accessToken')
      localStorage.removeItem('refreshToken')
      state.user = null
      state.accessToken = null
      state.refreshToken = null
    },
    setProducts(state, products) {
      state.products = products
    },
    addItemToCart(state, cartItem) {
      if (state.cart.some(cartitem => cartitem.id === cartItem.id) === true) {
        console.log(cartItem)
        cartItem.amount++
      } else {
        cartItem.amount = 1
        state.cart.push(cartItem)
      }

    },
  },
  actions: {
    isTokenValid({ commit }) {
      return verifyToken(localStorage.getItem('accessToken')).then((response) => {
        if (response.status === 200) {
          commit('isTokenValid', true)
        }
      }).catch((err) => {
        console.log(err.response.data.detail); commit('isTokenValid', false)
      })

    },
    loadProducts({ commit }) {
      return loadProductsResults().then((response) => {
        console.log(response.data.response)
        commit('setProducts', response.data)
      })
    }
  },
  plugins: [createPersistedState()]
})
