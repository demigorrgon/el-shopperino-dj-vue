<template>
  <div class="root">
    <p>wasda</p>
    <button @click="verify">verify jwt</button>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Home",
  data: () => {
    return {};
  },
  computed: {
    ...mapState(["tokenValid"]),
  },

  methods: {
    verify() {
      console.log(this.$store.dispatch("isTokenValid"));
    },
  },
};
</script>

<style>
</style>