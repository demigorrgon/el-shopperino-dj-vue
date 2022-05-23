import Vue from 'vue'
import Vuex from 'vuex'
import { verifyToken, loadProductsResults, getUsersOrders, getCategoriesList } from '@/api/shortcuts'
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
    orders: [],
    favorites: [],
    categories: []

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
    },
    currentUserOrders(state) {
      return state.orders
    },
    favoriteItems(state) {
      return state.favorites
    },
    getPaginationLength(state) {
      return state.products.total_pages
    }
  },
  mutations: {
    authorizeUser(state) {
      const decodedToken = jwt_decode(localStorage.getItem('accessToken'))
      // check if valid on top of it
      state.user = { "id": decodedToken.user_id, "username": decodedToken.username }
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
      state.orders = []
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
    removeItemFromCart(state, cartItemIndex) {
      // console.log(state.cart)
      console.log(state.cart[cartItemIndex])
      console.log(state.cart.splice(cartItemIndex, 1))
      // console.log(state.cart.forEach(item => item == cartItem))
    },
    emptyCartOnOrderSubmission(state) {
      state.cart = []
    },
    setCurrentUserOrders(state, orders) {
      state.orders = orders
    },
    // emptyOrders(state) {
    //   state.orders = []
    // }
    addItemToFavorites(state, product) {
      if (state.favorites.every((item) => item.id !== product.id) === true) {
        state.favorites.push(product)
      }
    },
    setCategories(state, categories) {
      state.categories = categories
    },
    setAmountOnItemInCart(state, index, amount) {
      console.log(index, amount)
      state.cart[index].amount = amount
    }
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
    },
    loadOrders({ commit, getters }) {
      return getUsersOrders(getters.activeUser.id).then((response) => {
        console.log(response)
        commit('setCurrentUserOrders', response.data.results)
      })
    },
    loadCategories({ commit }) {
      return getCategoriesList().then((response) => {
        console.log(response)
        commit('setCategories', response.data.results)
      })
    }
  },
  plugins: [createPersistedState()]
})
