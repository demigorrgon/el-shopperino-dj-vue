<template>
  <div class="root">
    <vs-row>
      <vs-col
        vs-type="flex"
        vs-justify="center"
        vs-align="center"
        vs-w="6"
        vs-offset="3"
        class="relogin-modal"
        v-if="isValid() === false"
      >
        <SessionExpired />
      </vs-col>
    </vs-row>
    <p>wasda</p>
    <button @click="verify">verify jwt</button>
    <div class="cart" v-if="toggleCart">
      <vs-row>
        <vs-col vs-w="6" vs-offset="3">
          <CartModal @closeCart="toggleCartVisible()" />
        </vs-col>
      </vs-row>
    </div>
    <br />
    <button @click="toggleCartVisible">cart</button>
    <br />
    <br />
    <br />
    <ProductItem />
  </div>
</template>

<script>
import CartModal from "../components/CartModal.vue";
import SessionExpired from "../components/SessionExpired.vue";
import ProductItem from "../components/ProductItem.vue";
import { mapGetters } from "vuex";
export default {
  name: "Home",
  components: {
    CartModal,
    SessionExpired,
    ProductItem,
  },
  data: () => {
    return {
      toggleCart: false,
    };
  },

  methods: {
    verify() {
      this.$store.dispatch("isTokenValid");
      if (this.$store.getters.tokenValid === false) {
        console.log("complain");
      }
    },
    isValid() {
      return this.$store.getters.tokenValid;
    },
    toggleCartVisible() {
      this.toggleCart = !this.toggleCart;
    },
  },
  computed: {
    ...mapGetters(["isTokenValid"]),
  },
};
</script>

<style>
</style>