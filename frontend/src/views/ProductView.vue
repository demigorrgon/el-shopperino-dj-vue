<template>
  <div class="product-wrapper">
    <vs-row vs-type="flex" class="main-row-wrapper">
      <vs-col vs-w="5" vs-offset="1" class="">
        <!-- <div class="image-part"> -->
        <img :src="pageData.image" class="product-pic" />
        <!-- </div> -->
      </vs-col>
      <vs-col vs-w="5" class="description-part" style="margin-left: 50px">
        <!-- {{ pageData }} -->
        <p class="product-title" align="left">{{ pageData.name }}</p>
        <p class="product-description" align="left">
          {{ pageData.description }}
        </p>
        <p class="product-price" align="left">${{ pageData.price }}</p>
        <vs-row vs-type="flex" vs-justify="center">
          <vs-button
            color="success"
            type="gradient"
            class="add-to-cart-button"
            @click="addToCart"
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
      </vs-col>
    </vs-row>
    <vs-divider color="dark" class="divider"
      ><p><i>You might also like:</i></p></vs-divider
    >
    <vs-row>
      <vs-col v-for="item in 4" :key="item" class="suggestion-wrapper" vs-w="3">
        <vs-row vs-type="space-inbetween">
          <img
            src="http://127.0.0.1:8000/media/images/angry_cat.png"
            class="suggestion-pic"
          />
          <p style="color: blue">
            <b
              ><i><router-link to="#">Placeholder title</router-link></i></b
            >
          </p>
          <p style="padding: 20px 50px 20px 50px; font-size: 14px">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
            eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim
            ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
            aliquip ex ea commodo consequat. Duis aute irure dolor in
            reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
            pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
            culpa qui officia deserunt mollit anim id est laborum.
          </p>
          <p>$654.00</p>
        </vs-row>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
import { getProductBySlug } from "../api/shortcuts.js";
import { mapMutations } from "vuex";
export default {
  components: {},
  data: () => {
    return {
      productSlug: null,
      pageData: {},
    };
  },
  created() {
    this.productSlug = this.$route.params.slug;
    getProductBySlug(this.productSlug).then((response) => {
      this.pageData = response.data;
    });
  },
  methods: {
    addToCart() {
      this.$store.commit("addItemToCart", this.pageData);
    },
    addToFavorites() {
      this.$store.commit("addItemToFavorites", this.pageData);
    },
  },
  computed: {
    ...mapMutations(["addItemToCart", "addItemToFavorites"]),
  },
};
</script>

<style>
p {
  font-family: "Montserrat", sans-serif;
  font-size: 18px;
}
.main-row-wrapper {
  margin-top: 20px;
}
/* .image-part {
  margin-left: 20px;
  border: 1px solid gray;
  padding: 10px 50px 50px 50px;
  margin: 10px 50px 50px 50px;

  height: 500px;
} */
.product-pic {
  width: 50%;
}
.description-part {
  /* border: 1px solid gray; */
  padding-top: 100px;
  padding-left: 50px;
  padding-right: 50px;
}
.product-title {
  margin-bottom: 20px;
  margin-top: 20px;
  font-weight: bold;
}

.product-price {
  font-weight: 700;
  margin-top: 20px;
}
.add-to-cart-button {
  margin-right: 20px;
}
.divider {
  padding-top: 50px;
}
.suggestion-wrapper {
  border: 1px solid gray;
  padding-left: 20px;
  /* margin: 20px 100px 20px 100px; */
}
.suggestion-pic {
  width: 20%;
}
</style>