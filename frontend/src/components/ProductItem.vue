<template>
  <div class="products-wrapper">
    <p>Filter by category:</p>
    <vs-row vs-type="flex" vs-justify="center">
      <div v-for="category in categories" :key="category.id">
        <vs-button
          color="dark"
          type="filled"
          class="category-btn"
          @click="filterByCategory(category.name)"
          >{{ category.name }}</vs-button
        >
      </div></vs-row
    >
    <vs-row v-if="isFiltered === false">
      <vs-col
        vs-type="flex"
        vs-align="flex-start"
        vs-justify="flex-start"
        vs-w="9"
        vs-offset="2"
        style="border: 1px solid gray"
      >
        <vs-col
          vs-type="flex"
          vs-justify="center"
          vs-w="2"
          v-for="(product, index) in products['results']"
          :key="product[index]"
          style="margin-right: 30px; margin-left: 30px; margin-bottom: 30px"
        >
          <ProductCard :product="product" />
        </vs-col>
      </vs-col>
    </vs-row>
    <vs-row v-else>
      <vs-col
        vs-type="flex"
        vs-align="flex-start"
        vs-justify="flex-start"
        vs-w="9"
        vs-offset="2"
        style="border: 1px solid gray"
      >
        <vs-col
          vs-type="flex"
          vs-justify="center"
          vs-w="2"
          v-for="(product, index) in filteredProducts"
          :key="product[index]"
          style="margin-right: 30px; margin-left: 30px; margin-bottom: 30px"
        >
          <ProductCard :product="product" />
        </vs-col>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
import ProductCard from "../components/ProductCard.vue";
import { mapMutations, mapActions } from "vuex";
export default {
  data: () => {
    return {
      products: null,
      categories: [],
      filteredProducts: [],
      isFiltered: false,
      // currentPage: 1,
    };
  },
  components: {
    ProductCard,
  },
  computed: { ...mapMutations(["setProducts"]) },
  methods: {
    ...mapActions(["loadProducts"]),
    filterByCategory(categoryName) {
      // console.log(this.products, categoryName);
      this.filteredProducts = this.products.results.filter(
        (product) => product.category === categoryName
      );
      this.isFiltered = !this.isFiltered;
    },
  },
  created() {
    this.$store.dispatch("loadProducts");
    this.$store.dispatch("loadCategories");
    this.products = this.$store.state.products;
    this.categories = this.$store.state.categories;
  },
};
</script>

<style>
.products-wrapper {
  margin-top: 30px;
}
.category-btn {
  margin: 10px 20px 20px 10px;
}
#app > div > div:nth-child(9) > div > div.vs-row > div > div {
  margin: 0 auto;
}
</style>