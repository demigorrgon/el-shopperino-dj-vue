<template>
  <div class="verify">
    <vs-row>
      <vs-col>
        <p style="margin-top: 20px">
          {{ this.serverResponse }}
        </p>
        <p>Redirecting in 3s...</p>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
import { verifyEmailCode } from "../api/shortcuts";
export default {
  data() {
    return {
      codeValid: null,
      serverResponse: "",
    };
  },
  methods: {
    verifyEmailCodeValid() {
      verifyEmailCode(this.$route.params.emailCode)
        .then((response) => (this.serverResponse = response.data.response))
        .catch((e) => (this.serverResponse = e.response.data.response));

      setTimeout(() => this.$router.push("/"), 3000);
    },
  },
  mounted() {
    // add vuex verification if mail was already sent b4 etc
    this.verifyEmailCodeValid();
  },
};
</script>

<style>
</style>