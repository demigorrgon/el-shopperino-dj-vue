<template>
  <div class="profile">
    <vs-row class="wrapper" vs-align="flex-start">
      <vs-col vs-w="2" vs-offset="1" class="left-part">
        <vs-row>
          <vs-col class="profile-menu">
            <vs-row vs-justify="center" class="menu-item"
              ><p @click="credentials">Credentials</p></vs-row
            >

            <vs-row vs-justify="center" class="menu-item"
              ><p @click="favorites">My favorites</p></vs-row
            >
            <vs-row vs-justify="center" class="menu-item"
              ><p @click="orders">My orders</p></vs-row
            ></vs-col
          >
        </vs-row>
      </vs-col>
      <vs-col vs-w="6" vs-offset="1" class="right-part">
        <div v-if="showCredentials">
          <p class="credentials-tooltip">
            <b><i>Edit profile:</i></b>
          </p>
          <div class="credentials-form">
            <ClientCredentialsForm />
          </div>
          <vs-button color="dark" type="border">Submit</vs-button>
        </div>
        <div v-if="showFavorites">
          <p class="favorites-tooltip">Favorite items</p>
          <vs-row
            v-for="(item, index) in favoriteItems"
            :key="index"
            vs-align="center"
            vs-justify="center"
            class="favorite-item"
          >
            <vs-divider />
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
        </div>
        <div v-if="showOrders">
          <p class="credentials-tooltip">
            <b><i>Orders:</i></b>
            <vs-row>
              <vs-col>
                <vs-row
                  v-for="order in this.$store.getters.currentUserOrders"
                  :key="order.id"
                >
                  <vs-divider />
                  <vs-col class="order-wrapper">
                    <vs-row
                      vs-type="flex"
                      vs-align="center"
                      vs-justify="center"
                    >
                      <vs-col
                        vs-type="flex"
                        vs-align="center"
                        vs-justify="center"
                        v-if="order.delivered === true"
                      >
                        <p class="order-text">Order: #{{ order.id }}</p>
                        <vs-chip class="delivery-status" color="success">
                          Delivered
                        </vs-chip>
                      </vs-col>
                      <vs-col
                        vs-type="flex"
                        vs-align="center"
                        vs-justify="center"
                        v-else
                      >
                        <p class="order-text">Order: #{{ order.id }}</p>
                        <vs-chip class="delivery-status" color="danger">
                          Not delivered
                        </vs-chip>
                      </vs-col>
                    </vs-row>
                    <vs-row
                      v-for="(item, index) in order.items"
                      :key="index"
                      vs-align="center"
                      vs-justify="flex-start"
                      class="order-item"
                    >
                      <vs-col
                        vs-type="flex"
                        vs-align="center"
                        vs-justify="flex-start"
                      >
                        <img :src="item.image" class="order-pic" />
                        <vs-col
                          vs-type="flex"
                          vs-w="2"
                          vs-align="center"
                          vs-justify="center"
                        >
                          <p class="order-text">
                            <a href="#">{{ item.product }}</a> <br />${{
                              item.price
                            }}
                            <br />{{ item.quantity }}
                            items total
                          </p></vs-col
                        >
                      </vs-col>
                    </vs-row>
                    <p class="order-text">Created at: {{ order.created_at }}</p>
                    <p class="order-text">Total: ${{ order.total_price }}</p>
                  </vs-col>
                </vs-row>
              </vs-col>
            </vs-row>
          </p>
        </div>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
import ClientCredentialsForm from "../components/ClientCredentialsForm.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  data: () => {
    return {
      active: true,
      showCredentials: true,
      showFavorites: false,
      showOrders: false,
    };
  },
  components: {
    ClientCredentialsForm,
  },
  methods: {
    credentials() {
      this.showFavorites = false;
      this.showOrders = false;
      this.showCredentials = true;
    },
    favorites() {
      this.showCredentials = false;
      this.showOrders = false;
      this.showFavorites = true;
    },
    orders() {
      this.showCredentials = false;
      this.showFavorites = false;
      this.showOrders = true;
    },
    loadOrdersInProfile() {
      this.$store.dispatch("loadOrders");
    },
    // nuke() {
    //   this.$store.commit("emptyOrders");
    // },
  },
  computed: {
    ...mapActions(["loadOrders"]),
    ...mapGetters(["favoriteItems"]),
  },
  created() {
    this.loadOrdersInProfile();
  },
};
</script>

<style>
p {
  font-family: "Montserrat", sans-serif;
  /* font-weight: bold; */
}
.wrapper {
  margin-top: 20px;
}
.left-part {
  opacity: 0.85;
  box-shadow: 0 0 2px 2px rgba(0, 0, 0, 0.2);
  border-radius: 5px;
  overflow: hidden;
}
.right-part {
  /* border: 1px solid gray; */
}
.profile-menu {
  height: 175px;
}
.menu-item {
  margin: 10px 0px 10px;
  border-bottom: 0.5px solid gray;
  transition: all 0.5s ease;
  color: gray;
  border: 3px solid white;
  font-family: "Montserrat", sans-serif;
  text-transform: uppercase;
  text-align: center;
  line-height: 1;
  font-size: 17px;
  background-color: transparent;
  padding: 10px;
  outline: none;
  border-radius: 4px;
}
.menu-item:hover {
  color: #001f3f;
  background-color: #d3d3d3;
  cursor: pointer;
}
.credentials-tooltip {
  margin-top: 10px;
}
.credentials-form {
  display: flex;
  margin-left: 100px;
}
.ul {
  list-style-type: none;
  padding: 0; /* Remove padding */
  margin: 0;
}
.order-wrapper {
  padding: 10px 10px 10px 10px;
}
.order-item {
  margin-bottom: 10px;
  margin-left: 15%;
}
.order-pic {
  width: 10%;
}
.order-text {
  font-weight: bold;
  margin-left: 20px;
}
.delivery-status {
  margin-left: 20px;
  transform: scale(0.9);
}

.favorites-tooltip {
  margin-bottom: 20px;
  font-weight: bold;
  font-style: italic;
}
.favorite-item {
  margin-bottom: 10px;
}
</style>