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
        <img src="@/assets/goblin-head.png" />
      </vs-navbar-title>
    </div>
    <div class="item-wrapper">
      <vs-navbar-item index="0">
        <a href="#" v-if="activeUser === null">Home</a>
        <a href="#" v-else><i>{{ this.$store.state.user }}</i></a>
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
</template>

<script>
import { mapGetters, mapState, mapMutations } from "vuex";
export default {
  computed: {
    ...mapGetters(["activeUser", "tokenValid"]),
    ...mapState(["isTokenValid"]),
  },
  //   created() {
  //     this.$store.dispatch("isTokenValid");
  //     if (this.$store.getters.tokenValid === false) {
  //       this.$store.commit("logout");
  //     }
  //   },
  methods: {
    ...mapMutations(["logout"]),
  },
};
</script>

<style>
</style>