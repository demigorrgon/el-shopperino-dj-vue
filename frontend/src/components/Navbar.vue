<template>
  <vs-navbar
    color="black"
    text-color="white"
    active-text-color="white"
    class="myNavbar"
    style="border-radius: 0px 0px 20px 20px"
  >
    <div slot="title">
      <vs-navbar-title style="margin-left: 100px">
        <router-link to="/">
          <img src="@/assets/goblin-head.png" class="logo"
        /></router-link>
      </vs-navbar-title>
    </div>
    <div class="item-wrapper">
      <vs-navbar-item index="0">
        <router-link to="/" v-if="activeUser === null">Home</router-link>
        <!-- <a href="#" v-if="activeUser === null">Home</a> -->
        <router-link to="/profile" v-else
          ><i>{{ this.$store.state.user.username }}</i></router-link
        >

        <!-- <a href="/profile" v-else
          ><i>{{ this.$store.state.user.username }}</i></a
        > -->
      </vs-navbar-item>
      <vs-spacer></vs-spacer>
      <vs-navbar-item index="1" v-if="activeUser === null">
        <router-link to="/login">Login</router-link>
      </vs-navbar-item>
      <vs-navbar-item index="2" v-if="activeUser === null">
        <router-link to="/register">Register</router-link>
      </vs-navbar-item>
      <vs-navbar-item index="2" v-if="activeUser !== null">
        <a href="#" @click="logout">Logout</a>
      </vs-navbar-item>
      <vs-navbar-item index="3" v-if="activeUser !== null">
        <a href="#" @click="toggleCart()">Cart</a>
      </vs-navbar-item>
      <vs-navbar-item index="4" v-if="activeUser !== null">
        <router-link to="/favorites">Favorites</router-link>
      </vs-navbar-item>
    </div>
  </vs-navbar>
</template>

<script>
import { mapGetters, mapState, mapMutations } from "vuex";

export default {
  data: () => {
    return {};
  },
  computed: {
    ...mapGetters(["activeUser", "tokenValid"]),
    ...mapState(["isTokenValid"]),
  },
  methods: {
    ...mapMutations(["logout"]),
    logout() {
      this.$store.commit("logout");
    },
    // toggleCart() {
    //   this.open = !this.open;
    // },
    toggleCart() {
      this.$emit("closeCart");
    },
  },
};
</script>

<style>
</style>