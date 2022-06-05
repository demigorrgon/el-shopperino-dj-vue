<template>
  <div class="home">
    <h1>Login</h1>
    <br />
    <form>
      <vs-row>
        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12"
          ><vs-input
            class="inputx"
            placeholder="Username"
            style="margin-bottom: 10px"
            v-model="username"
          />
        </vs-col>
        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12"
          ><vs-input
            class="inputx"
            placeholder="Password"
            style="margin-bottom: 10px"
            type="password"
            v-model="password"
          />
        </vs-col>
        <vs-col vs-type="flex" vs-justify="center" vs-align="center" vs-w="12">
          <vs-button color="dark" type="border" @click="login">Login</vs-button>
          <!-- <button type="submit">Login</button> -->
        </vs-col>
        <vs-col style="margin-top: 10px"><a href="#">Register?</a></vs-col>
      </vs-row>
    </form>
  </div>
</template>

<script>
// import { obtainToken } from "../api/shortcuts.js";
import { mapActions, mapMutations } from "vuex";
export default {
  data: () => {
    return { username: "", password: "" };
  },
  components: {},
  methods: {
    ...mapMutations(["setAccessToken", "setRefreshToken", "authorizeUser"]),
    ...mapActions(["loginUser"]),
    login() {
      this.loginUser({ username: this.username, password: this.password });
      this.$router.push("/");
    },
  },
};
</script>

<style>
</style>