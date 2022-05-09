<template>
  <vs-alert title="Danger" active="true" color="warning">
    Pls <router-link to="/login">relogin</router-link>, your session expired
  </vs-alert>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  computed: {
    ...mapGetters(["tokenValid"]),
  },
};
</script>

<style>
</style>