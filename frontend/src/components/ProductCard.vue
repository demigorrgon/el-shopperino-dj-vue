<template>
  <div class="product-card">
    <img class="product-pic" :src="product.image" />
    <br />
    <h2>
      <router-link :to="'/product/' + product.slug">
        {{ product.name }}</router-link
      >
    </h2>
    <br />
    <p class="product-price">${{ product.price }}</p>
    <p class="product-description">{{ product.description }}</p>
    <vs-row class="btns-wrapper">
      <vs-button
        color="success"
        type="gradient"
        style="margin-bottom: 10px"
        @click="addToCart"
        class="add-to-cart-btn"
        >Add to cart</vs-button
      >
      <vs-button
        radius
        color="danger"
        type="gradient"
        icon="favorite"
        @click="addToFavorites"
      ></vs-button
    ></vs-row>
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
    addToFavorites() {
      this.$store.commit("addItemToFavorites", this.$props.product);
    },
  },
  computed: {
    ...mapMutations(["addItemToCart", "addItemToFavorites"]),
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
.btns-wrapper {
  margin-left: 30px;
}

.add-to-cart-btn {
  margin-right: 30px;
}
</style>