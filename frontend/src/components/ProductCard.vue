<template>
  <div class="product-card">
    <img class="product-pic" :src="product.image" />
    <br />
    <h2>{{ product.name }}</h2>
    <br />
    <p class="product-price">${{ product.price }}</p>
    <p class="product-description">{{ product.description }}</p>
    <vs-button
      color="success"
      type="gradient"
      style="margin-bottom: 10px"
      @click="addToCart()"
      >Add to cart</vs-button
    >
  </div>
</template>

<script>
import { mapMutations } from "vuex";
export default {
  props: ["product"],
  methods: {
    addToCart() {
      this.$store.commit("addItemToCart", this.$props.product);
    },
  },
  computed: {
    ...mapMutations(["addItemToCart"]),
  },
};
</script>

<style scoped>
.product-pic {
  width: 90% !important;
}
.product-card {
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  max-width: 300px;
  margin: auto;
  text-align: center;
  padding: 10px 10px 10px 10px;
  /* font-family: arial; */
  /* border: 1px solid red; */
}

.product-price {
  color: grey;
  font-size: 22px;
  margin-bottom: 20px;
}

/* .product-card {
  border: none;
  outline: 0;
  padding: 12px;
  color: white;
  background-color: #000;
  text-align: center;
  cursor: pointer;
  width: 100%;
  font-size: 18px;
}
*/
.product-description {
  margin-bottom: 20px;
}
.product-card:hover {
  opacity: 0.9;
  transition-duration: 0.5s;
}
</style>