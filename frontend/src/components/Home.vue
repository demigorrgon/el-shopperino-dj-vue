<template>
  <div class="root">
    <p>wasda</p>
    <button @click="verify">verify jwt</button>
  </div>
</template>

<script>
export default {
  name: "Home",
  data: () => {
    return {};
  },

  methods: {
    verify() {
      this.$store.dispatch("isTokenValid");
      if (this.$store.getters.tokenValid === false) {
        console.log("complain");
      }
    },
  },
};
</script>

<style>
</style>