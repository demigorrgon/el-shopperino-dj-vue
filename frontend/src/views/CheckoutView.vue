<template>
  <div class="checkout">
    <vs-row>
      <vs-col
        vs-w="6"
        vs-type="flex"
        vs-align="center"
        vs-justify="flex-start"
        style="flex-direction: column; border: 1px solid gray"
      >
        <p class="order-tooltip">
          <i>Fill next fields to complete your order:</i>
        </p>
        <ClientCredentialsForm
      /></vs-col>
      <!-- </vs-col> -->
      <vs-col vs-w="6">
        <vs-col vs-w="6" vs-offset="3" style="border: 1px solid gray">
          <p class="cart-tooltip"><i>Your order:</i></p>
          <vs-row
            vs-align="center"
            vs-justify="center"
            v-for="item in this.itemsInCart"
            :key="item.id"
            style="border: 1px solid red; margin-bottom: 10px"
          >
            <vs-col vs-w="3"
              ><img class="order-picture" :src="item.image"
            /></vs-col>
            <vs-col vs-w="3"
              ><p>
                <router-link :to="'/product/' + item.slug">{{
                  item.name
                }}</router-link>
                - x{{ item.amount }}
              </p></vs-col
            >
            <vs-col vs-w="3"
              ><p>${{ item.price }}</p></vs-col
            >
            <vs-col vs-w="3">${{ item.price * item.amount }}</vs-col>
          </vs-row>
          <p>Total to pay: ${{ orderTotalPrice }}</p>
          <vs-button class="confirm" color="dark" @click="submitOrder"
            >Confirm order</vs-button
          >
        </vs-col>
      </vs-col>
    </vs-row>
    <div class="error-modal" v-if="notLoggedInError">
      <ErrorModal @close="toggleError" />
    </div>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";
import ErrorModal from "../components/ErrorModal.vue";
import ClientCredentialsForm from "../components/ClientCredentialsForm.vue";
import { sendOrder } from "../api/shortcuts.js";
export default {
  data: () => {
    return {
      orderTotalPrice: 0,

      notLoggedInError: false,
    };
  },
  components: { ErrorModal, ClientCredentialsForm },
  computed: {
    ...mapGetters(["itemsInCart", "activeUser", "tokenValid"]),
    ...mapMutations(["emptyCartOnOrderSubmission"]),
  },
  methods: {
    totalPrice() {
      let sum = 0;
      this.$store.getters.itemsInCart.forEach(
        (item) => (sum += item.amount * item.price)
      );
      return sum;
    },
    submitOrder() {
      let payload = {};
      let items = [];
      for (let item in this.itemsInCart) {
        console.log();
        items.push({
          product: this.itemsInCart[item].id,
          quantity: this.itemsInCart[item].amount,
        });
        // payload["product"] = item.id;
        // payload["quantity"] = item.amount;
      }
      try {
        payload["items"] = items;
        payload["customer"] = this.activeUser.id;
        payload["total_price"] = this.orderTotalPrice;

        sendOrder(payload).then((response) => {
          if (response.status === 201) {
            this.$router.push("/checkout/success");
            this.$store.commit("emptyCartOnOrderSubmission");
          }
        });
      } catch (error) {
        console.log(error);
        this.notLoggedInError = !this.notLoggedInError;
      }
    },
    toggleError() {
      this.notLoggedInError = !this.notLoggedInError;
    },
  },
  created() {
    this.orderTotalPrice = this.totalPrice();
    if (this.tokenValid === false) {
      this.toggleError();
    }
  },
};
</script>

<style>
p {
  font-family: "Montserrat", sans-serif;
}
.order-tooltip {
  font-size: 18px;
  margin-top: 30px;
  margin-bottom: 20px;
}
.cart-tooltip {
  font-size: 18px;
  margin-top: 30px;
  margin-bottom: 20px;
}

.confirm {
  margin-top: 20px;
}
.order-picture {
  width: 50%;
}
</style>