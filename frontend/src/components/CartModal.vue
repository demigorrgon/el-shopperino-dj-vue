<template>
  <div class="modal-cart">
    <div class="modal-content">
      <vs-row ws-w="2">
        <vs-col vs-w="12" vs-offset="11">
          <span class="close" @click="toggleCart()">
            <vs-button
              color="danger"
              class="close-button"
              style="height: 35px; width: 35px; border-radius: 10px"
              >x</vs-button
            ></span
          >
        </vs-col>
      </vs-row>
      <div>
        <!-- <p>Cart I guess</p> -->

        <div v-for="(item, index) in itemsInCart" :key="item[index]">
          <vs-row vs-align="center" vs-justify="center">
            <vs-col style="display: inline-flex">
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
                  :placeholder="$store.getters.itemsInCart[index].amount"
                  class="items-amount-cart"
                  :danger="danger"
                  danger-text="Are you sure you want THAT much? Current limit - 20"
                  v-model="amount[index]"
                  @input="checkout"
                />
              </vs-col>
              <!-- <p style="margin-left: 10px">{{ amount }}</p>
              <p>{{ item.price * amount[index] }}</p> -->
            </vs-col>
          </vs-row>
          <br />
        </div>

        <p>Total: ${{ totalPrice }}</p>
        <button @click="checkout()">checkout</button>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapState } from "vuex";
export default {
  data: () => {
    return {
      amount: [],
      totalPrice: 0,
      danger: false,
    };
  },
  methods: {
    toggleCart() {
      this.$emit("closeCart");
    },
    checkout() {
      let totalPrice = 0;

      for (let index in this.itemsInCart) {
        if (
          isNaN(this.amount[index]) ||
          this.amount[index] === null ||
          this.amount[index] === ""
        ) {
          totalPrice +=
            this.itemsInCart[index].amount * this.itemsInCart[index].price;
        } else if (this.amount[index] >= 20) {
          this.danger = true;
          totalPrice += this.amount[index] * this.itemsInCart[index].price;
        } else {
          this.danger = false;
          totalPrice += this.amount[index] * this.itemsInCart[index].price;
        }
      }
      this.totalPrice = totalPrice;
    },
  },
  computed: {
    ...mapGetters(["itemsInCart"]),
    ...mapState(["cart"]),
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
  border: 1px solid #888;
  width: 80%;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);
  animation-name: animatetop;
  animation-duration: 0.4s;
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