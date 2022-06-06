<template>
  <div id="app">
    <Navbar @closeCart="toggleCart" />
    <vs-row>
      <vs-col
        vs-type="flex"
        vs-justify="center"
        vs-align="center"
        vs-w="6"
        vs-offset="3"
        class="relogin-modal"
        v-if="isValid() === false"
      >
        <SessionExpired />
      </vs-col>
    </vs-row>

    <CartModal @closeCartInChild="toggleCart" v-if="showCartModal" />

    <router-view />
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import Navbar from "@/components/Navbar.vue";
import CartModal from "./components/CartModal.vue";
import SessionExpired from "./components/SessionExpired.vue";

export default {
  components: { Navbar, CartModal, SessionExpired },
  data() {
    return {
      showCartModal: false,
    };
  },
  mounted() {
    this.$store.dispatch("isTokenValid");
    if (this.$store.getters.tokenValid === false) {
      this.$store.commit("logout");
    }
  },
  methods: {
    toggleCart() {
      this.showCartModal = !this.showCartModal;
    },
    isValid() {
      return this.$store.getters.tokenValid;
    },
  },
  computed: {
    ...mapGetters(["activeUser", "isTokenValid"]),
  },
};
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

a:hover {
  text-decoration: underline;
}
nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}

.logo {
  width: 10%;
}

.item-wrapper {
  display: flex;
  margin-right: 100px;
}

.relogin-modal {
  /* border: 1px solid gray; */
  display: flex;
  margin: 0px 300px 20px 300px;
}
</style>
