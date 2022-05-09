<template>
  <div id="app">
    <!-- <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/login">Login</router-link>
    </nav>
    <router-view /> -->
    <vs-navbar
      v-model="indexActive"
      color="black"
      text-color="white"
      active-text-color="white"
      class="myNavbar"
      style="border-radius: 0px 0px 20px 20px"
    >
      <div slot="title">
        <vs-navbar-title style="margin-left: 100px">
          <img src="@/assets/goblin-head.png" />
        </vs-navbar-title>
      </div>
      <div class="item-wrapper">
        <vs-navbar-item index="0">
          <a href="#" v-if="activeUser === null">Home</a>
          <a href="#" v-else>Some user</a>
        </vs-navbar-item>
        <vs-spacer></vs-spacer>
        <vs-navbar-item index="1" v-if="activeUser === null">
          <!-- <a href="#">News</a> -->
          <router-link to="/login">Login</router-link>
        </vs-navbar-item>
        <vs-navbar-item index="2">
          <a href="#">Cart</a>
        </vs-navbar-item>
      </div>
    </vs-navbar>
    <router-view />
  </div>
</template>
<script>
import { mapGetters } from "vuex";
export default {
  data: () => {
    return {
      // isLoggedIn: this.isLoggedIn,
    };
  },
  methods: {},
  computed: { ...mapGetters(["activeUser"]) },
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

img {
  width: 10%;
}

.item-wrapper {
  display: flex;
  margin-right: 100px;
}
</style>
