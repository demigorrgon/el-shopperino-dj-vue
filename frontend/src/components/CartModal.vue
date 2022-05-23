<template>
  <div class="modal-cart">
    <div class="modal-content">
      <vs-row ws-w="2">
        <vs-col vs-w="12" vs-offset="11">
          <span class="close" @click="toggleCart()">
            <vs-button
              radius
              color="danger"
              class="close-button"
              icon="close"
              style="height: 35px; width: 35px"
            ></vs-button
          ></span>
        </vs-col>
      </vs-row>
      <div>
        <div v-for="(item, index) in itemsInCart" :key="item[index]">
          <vs-row vs-align="center" vs-justify="center">
            <vs-col style="display: inline-flex" vs-align="center">
              <vs-col vs-w="1">
                <img :src="item.image" class="cart-picture" />
              </vs-col>
              <vs-col vs-w="4">
                <p class="cart-description">
                  <a :href="item.slug">{{ item.name }}</a> - ${{ item.price }}
                </p>
              </vs-col>
              <vs-col vs-w="3">
                <vs-input
                  type="number"
                  class="items-amount-cart"
                  :placeholder="cart[index].amount"
                  :danger="danger"
                  danger-text="Are you sure you want THAT much? Current limit - 20"
                  v-model="amounts[index]"
                  @input="updateCart($event, index)"
                />
              </vs-col>
              <vs-button
                radius
                color="danger"
                type="gradient"
                icon="close"
                style="margin-left: 20px; height: 85%"
                @click="removeFromCart(index)"
              ></vs-button>
            </vs-col>
          </vs-row>
          <br />
        </div>

        <p
          style="margin-bottom: 10px"
          v-if="isNaN(totalPrice) === false && amounts.length > 0"
        >
          Total: ${{ totalPrice }}
        </p>
        <vs-button
          color="dark"
          type="filled"
          @click="confirmCheckout()"
          style="margin-bottom: 10px"
          >Checkout</vs-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState, mapMutations } from "vuex";
export default {
  data: () => {
    return {
      amounts: [],
      totalPrice: 0,
      danger: false,
    };
  },
  methods: {
    toggleCart() {
      this.$emit("closeCartInChild");
    },
    checkout() {
      let totalPrice = 0;

      for (let index in this.itemsInCart) {
        if (
          isNaN(this.amounts[index]) ||
          this.amounts[index] === null ||
          this.amounts[index] === ""
        ) {
          totalPrice +=
            this.itemsInCart[index].amounts * this.itemsInCart[index].price;
        } else if (this.amounts[index] > 20) {
          this.danger = true;
          this.amounts[index] = 20;
          totalPrice += this.amounts[index] * this.itemsInCart[index].price;
        } else {
          if (this.amounts[index] < 1) {
            this.amounts[index] = 1;
          }
          this.danger = false;
          totalPrice += this.amounts[index] * this.itemsInCart[index].price;
        }
      }
      this.totalPrice = totalPrice;
    },
    removeFromCart(index) {
      this.$store.commit("removeItemFromCart", index);
    },
    updateCart() {
      this.checkout();
    },
    confirmCheckout() {
      for (let index in this.amounts) {
        this.cart[index].amount = this.amounts[index];
      }
      this.$router.push("/checkout");
      this.toggleCart();
    },
  },
  computed: {
    ...mapGetters(["itemsInCart"]),
    ...mapState({
      cart: (state) => state.cart,
    }),
    ...mapMutations(["removeItemFromCart", "setAmountOnItemInCart"]),
  },
  mounted() {
    for (let item in this.itemsInCart) {
      this.amounts.push(this.itemsInCart[item].amount);
    }
  },
};
</script>

<style>
/* .modal-cart {
  display: block;
  position: fixed; 
  z-index: 1; 
  left: 0;
  top: 0;
  width: 100%; 
  height: 100%; 
  overflow: auto; 
  background-color: rgb(0, 0, 0); 
  background-color: rgba(0, 0, 0, 0.4); 
} */
.modal-header {
  padding: 2px 16px;
  background-color: #5cb85c;
  color: white;
}

/* Modal Body */
.modal-body {
  padding: 2px 16px;
}

/* Modal Footer */
.modal-footer {
  padding: 2px 16px;
  background-color: #5cb85c;
  color: white;
}

/* Modal Content */
.modal-content {
  position: relative;
  background-color: #fefefe;
  margin: auto;
  padding: 0;
  width: 40%;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  animation-name: animatetop;
  animation-duration: 0.4s;
  border-radius: 3px;
  margin-top: 10px;
  margin-bottom: 30px;
}
.close-button {
  position: absolute;
  top: 0;
  right: 0;
}
.cart-description {
  overflow: hidden;
}
.cart-picture {
  float: left;
  width: 80%;
  margin-left: 10px;
}
::-webkit-input-placeholder {
  text-align: center;
}
.items-amount-cart {
  border-radius: 15px;
  text-align: center;
}

/* Add Animation */
@keyframes animatetop {
  from {
    top: -300px;
    opacity: 0;
  }
  to {
    top: 0;
    opacity: 1;
  }
}
</style>