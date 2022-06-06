<template>
  <div class="root">
    <!-- <Navbar @closeCart="toggleCartVisible()" /> -->

    <!-- <button @click="verify">verify jwt</button> -->
    <!-- <div class="cart" v-if="toggleCart">
      <vs-row>
        <vs-col vs-w="6" vs-offset="3">
          <CartModal @closeCart="toggleCartVisible()" />
        </vs-col>
      </vs-row>
    </div> -->
    <!-- <br />
    <button @click="toggleCartVisible">cart</button>
    <br />
    <br />
    <br /> -->
    <ProductItem />
    <vs-col vs-offset="-5">
      <vs-pagination
        :total="getPaginationLength"
        v-model="currentPage"
      ></vs-pagination>
    </vs-col>
  </div>
</template>

<script>
// import SessionExpired from "../components/SessionExpired.vue";
import ProductItem from "../components/ProductItem.vue";
import { mapGetters } from "vuex";
export default {
  name: "Home",
  components: {
    // SessionExpired,
    ProductItem,
  },
  data: () => {
    return {
      currentPage: 1,
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
    ...mapGetters(["isTokenValid", "getPaginationLength"]),
  },
  mounted() {
    this.$store.dispatch("loadProducts");
    this.$store.dispatch("loadOrders");
    this.$store.dispatch("loadCategories");
  },
};
</script>

<style>
</style>