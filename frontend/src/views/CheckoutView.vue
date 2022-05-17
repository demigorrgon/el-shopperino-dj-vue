<template>
  <div class="checkout">
    <Navbar />
    <vs-row>
      <vs-col vs-w="6">
        <vs-col
          vs-type="flex"
          vs-align="center"
          vs-justify="flex-start"
          style="flex-direction: column; border: 1px solid gray"
        >
          <vs-col
            vs-w="6"
            vs-offset="1"
            vs-align="flex-start"
            vs-justify="flex-start"
            style="text-align: justify"
          >
            <p class="order-tooltip">
              <i>Fill next fields to complete your order:</i>
            </p>
            <p class="input-helper">Full name:</p>
            <vs-input
              class="inputfield"
              placeholder="Full name"
              v-model="fullName"
            />
            <p class="input-helper">Phone number:</p>
            <vs-input
              class="inputfield"
              placeholder="Phone number"
              v-model="phoneNumber"
            />
            <p class="input-helper">Country:</p>
            <!-- <vs-input
              class="inputfield"
              placeholder="Country"
              v-model="country"
            /> -->
            <country-select
              v-model="country"
              :country="country"
              topCountry="US"
              class="country-dropdown"
            />
            <p class="input-helper">Region:</p>
            <!-- <vs-input
              class="inputfield"
              placeholder="Region"
              v-model="region"
            /> -->
            <region-select
              v-model="region"
              :country="country"
              :region="region"
              class="region-dropdown"
            />
            <p class="input-helper">Postal address:</p>
            <vs-input
              class="inputfield"
              placeholder="Postal address"
              v-model="address"
            />
          </vs-col>
          <vs-col
            vs-w="6"
            vs-offset="-2"
            vs-align="center"
            vs-justify="center"
            style="margin-right: 43px"
          >
            <vs-dropdown>
              <vs-button color="dark" class="btn-drop" icon="expand_more"
                >Choose delivery point</vs-button
              >

              <vs-dropdown-menu>
                <vs-dropdown-item> Option 1 </vs-dropdown-item>
                <vs-dropdown-item> Option 2 </vs-dropdown-item>
                <vs-dropdown-item> Option 3 </vs-dropdown-item>
              </vs-dropdown-menu>
            </vs-dropdown>

            <br />
          </vs-col>
        </vs-col>
      </vs-col>
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
              ><p>{{ item.name }} - x{{ item.amount }}</p></vs-col
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
import Navbar from "../components/Navbar.vue";
import ErrorModal from "../components/ErrorModal.vue";
import { sendOrder } from "../api/shortcuts.js";
export default {
  data: () => {
    return {
      orderTotalPrice: 0,
      fullName: null,
      phoneNumber: null,
      country: "",
      region: "",
      address: null,
      notLoggedInError: false,
    };
  },
  components: { Navbar, ErrorModal },
  computed: {
    ...mapGetters(["itemsInCart", "activeUser"]),
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
  },
};
</script>

<style scoped>
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
.input-helper {
  font-size: 11px;
  margin-left: 10px;
}
.inputfield {
  margin: 3px 0 10px 0px;
}
.confirm {
  margin-top: 20px;
}
.order-picture {
  width: 50%;
}
.country-dropdown {
  padding: 5px;
  border: 1px solid gray;
  border-radius: 6px;
  max-width: 200px;
  opacity: 0.6;
  margin-bottom: 7px;
}
.region-dropdown {
  padding: 5px;
  border: 1px solid gray;
  border-radius: 6px;
  max-width: 200px;
  opacity: 0.6;
  margin-bottom: 7px;
}
</style>