<template>
  <div class="register">
    <vs-row vs-type="flex" vs-justify="center">
      <vs-col style="width: 10% !important">
        <h1 style="margin-top: 20px; margin-bottom: 20px">Pls register:</h1>
        <vs-input color="#11e988" label-placeholder="Email" v-model="email" />
        <vs-input
          color="#11e988"
          label-placeholder="Username"
          v-model="username"
        />
        <vs-input
          color="#11e988"
          label-placeholder="Password"
          type="password"
          v-model="password"
        />

        <vs-input
          color="#11e988"
          label-placeholder="First Name"
          v-model="firstName"
        />
        <vs-input
          color="#11e988"
          label-placeholder="Last Name"
          v-model="lastName"
        />
        <vs-button color="dark" style="margin-top: 10px" @click="register"
          >Register</vs-button
        >
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
import { registerUser } from "../api/shortcuts";
import { mapActions, mapMutations, mapGetters } from "vuex";
export default {
  data() {
    return {
      username: "",
      email: "",
      password: "",
      firstName: "",
      lastName: "",
    };
  },
  methods: {
    ...mapMutations(["setNotVerifiedUser"]),
    ...mapActions(["loginUser"]),

    register() {
      registerUser(
        this.username,
        this.email,
        this.password,
        this.firstName,
        this.lastName
      ).then((response) => {
        this.$store.commit("setNotVerifiedUser", response.data);
      });
      // this.loginUser({
      //   username: this.username,
      //   password: this.password,
      // }).catch((e) => console.log(e));
      this.$router.push("/send-email");
    },
  },
  computed: {
    ...mapGetters(["activeUser"]),
  },
};
</script>

<style>
</style>