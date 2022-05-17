<template>
  <div id="app">
    <router-view />
  </div>
</template>
<script>
import { mapGetters } from "vuex";
// import Navbar from "@/components/Navbar.vue";
export default {
  components: {},
  mounted() {
    this.$store.dispatch("isTokenValid");
    if (this.$store.getters.tokenValid === false) {
      this.$store.commit("logout");
    }
  },
  methods: {},
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
