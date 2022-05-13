<template>
  <div>
    <vs-row>
      <vs-col
        vs-type="flex"
        vs-align="flex-start"
        vs-justify="flex-start"
        vs-w="9"
        vs-offset="2"
        style="border: 1px solid gray; flex-wrap: wrap"
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
      <vs-col vs-offset="-5">
        <vs-pagination
          :total="products['total_pages']"
          v-model="currentPage"
          :max="5"
        ></vs-pagination>
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
      currentPage: 1,
    };
  },
  components: {
    ProductCard,
  },
  computed: { ...mapMutations(["setProducts"]) },
  methods: {
    ...mapActions(["loadProducts"]),
  },
  created() {
    this.$store.dispatch("loadProducts");
    this.products = this.$store.state.products;
  },
};
</script>

<style>
#app > div > div:nth-child(9) > div > div.vs-row > div > div {
  margin: 0 auto;
}
</style>