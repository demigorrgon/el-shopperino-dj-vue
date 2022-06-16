<template>
  <div class="favorites">
    <vs-row>
      <vs-col class="favorites-wrapper" vs-w="6" vs-offset="3">
        <p class="favorites-text">Favorites:</p>
        <vs-row
          v-for="(item, index) in favoriteItems"
          :key="index"
          vs-align="center"
          vs-justify="center"
          class="order-item"
        >
          <vs-col vs-type="flex" vs-align="center" vs-justify="center">
            <img :src="item.image" class="order-pic" />
            <vs-col
              vs-type="flex"
              vs-w="2"
              vs-align="center"
              vs-justify="center"
            >
              <p class="order-text">
                <a href="#">{{ item.name }}</a> <br />${{ item.price }}
              </p></vs-col
            >
          </vs-col>
        </vs-row>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
import { mapGetters } from "vuex";
export default {
  components: {},
  computed: {
    ...mapGetters(["favoriteItems"]),
  },
};
</script>

<style scoped>
.favorites-wrapper {
  margin-top: 20px;
  /* border: 1px solid gray; */
}
.favorites-text {
  margin-bottom: 20px;
  font-family: "Montserrat", sans-serif;
  font-weight: bold;
}
.order-item {
  margin-left: 0px !important;
}
</style>