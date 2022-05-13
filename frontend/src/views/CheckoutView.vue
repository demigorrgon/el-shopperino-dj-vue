<template>
  <div class="checkout">
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
            <vs-input class="inputfield" placeholder="Full name" />
            <p class="input-helper">Phone number:</p>
            <vs-input class="inputfield" placeholder="Phone number" />
            <p class="input-helper">Country:</p>
            <vs-input class="inputfield" placeholder="Country" />
            <p class="input-helper">Region:</p>
            <vs-input class="inputfield" placeholder="Region" />
            <p class="input-helper">Postal address:</p>
            <vs-input class="inputfield" placeholder="Postal address" />
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

            <vs-button class="confirm" color="dark"
              >Confirm order</vs-button
            ></vs-col
          >
        </vs-col>
      </vs-col>
      <!-- </vs-col> -->
      <vs-col vs-w="6">
        <vs-col vs-w="6" vs-offset="3" style="border: 1px solid gray">
          <p class="cart-tooltip"><i>Your order:</i></p>
        </vs-col>
      </vs-col>
    </vs-row>
  </div>
</template>

<script>
export default {
  components: {},
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
</style>