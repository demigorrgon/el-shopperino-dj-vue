<template>
  <vs-alert title="Danger" active="true" color="danger">
    Pls <router-link to="/login">relogin</router-link>, your session expired
  </vs-alert>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  computed: {
    ...mapGetters(["tokenValid"]),
  },
  mounted() {
    this.$store.commit("logout");
  },
};
</script>

<style>
</style>