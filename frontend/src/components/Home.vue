<template>
  <div class="root">
    <p>wasda</p>
    <p>token - {{ accessToken }}</p>
    <button @click="verify">Verify</button>
  </div>
</template>

<script>
import { mapState } from "vuex";
import { verifyToken } from "@/api/shortcuts";
export default {
  name: "Home",
  data: () => {
    return {};
  },
  computed: {
    ...mapState(["accessToken", "refreshToken"]),
  },
  methods: {
    async verify() {
      await console.log(
        verifyToken(this.accessToken).then((response) => {
          console.log(response.status);
        })
      );
    },
  },
};
</script>

<style>
</style>