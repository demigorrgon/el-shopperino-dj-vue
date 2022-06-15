<template>
  <div class="send-mail">
    <vs-row>
      <vs-col>
        <p v-if="mailSent">
          Message with verification link was sent to your email, pls activate
          your account
        </p>
        <p v-else>Mail is being sent pls wait</p>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
import { sendVerificationEmail } from "../api/shortcuts";
export default {
  data() {
    return {
      mailSent: false,
    };
  },
  methods: {
    sendEmail() {
      sendVerificationEmail(
        this.notVerifiedUser["email"],
        this.notVerifiedUser.verify_email_link.split("/")[
          this.notVerifiedUser.verify_email_link.split("/").length - 1
        ]
      );
    },
  },
  computed: {
    ...mapGetters(["activeUser", "notVerifiedUser"]),
  },
  mounted() {
    this.sendEmail();
    this.mailSent = true;
    this.$store.commit("setNotVerifiedUser", {});
  },
};
</script>

<style>
</style>