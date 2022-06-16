<template>
  <div class="credentials">
    <vs-col
      vs-w="6"
      vs-offset="1"
      vs-align="flex-start"
      vs-justify="flex-start"
      style="text-align: justify"
    >
      <p class="input-helper">Full name:</p>
      <vs-input class="inputfield" placeholder="Full name" v-model="fullName" />
      <p class="input-helper">Phone number:</p>
      <vs-input
        class="inputfield"
        placeholder="Phone number"
        v-model="phoneNumber"
      />
      <p class="input-helper">Country:</p>
      <!-- <vs-input
              class="inputfield"
              placeholder="Country"
              v-model="country"
            /> -->
      <country-select
        v-model="country"
        :country="country"
        topCountry="US"
        class="country-dropdown"
      />
      <p class="input-helper">Region:</p>
      <!-- <vs-input
              class="inputfield"
              placeholder="Region"
              v-model="region"
            /> -->
      <region-select
        v-model="region"
        :country="country"
        :region="region"
        class="region-dropdown"
      />
      <p class="input-helper">Postal address:</p>
      <vs-input
        class="inputfield"
        placeholder="Postal address"
        v-model="address"
      />
      <!-- <vs-col vs-w="6" vs-offset="1" vs-align="center" vs-justify="center"> -->
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
    </vs-col>
  </div>
</template>

<script>
export default {
  data: () => {
    return {
      fullName: null,
      phoneNumber: null,
      country: "",
      region: "",
      address: null,
    };
  },
};
</script>

<style>
p {
  font-family: "Montserrat", sans-serif;
}

.input-helper {
  font-size: 11px;
  margin-left: 10px;
}
.inputfield {
  margin: 3px 0 10px 0px;
}
.country-dropdown {
  padding: 5px;
  border: 1px solid gray;
  border-radius: 6px;
  max-width: 200px;
  opacity: 0.6;
  margin-bottom: 7px;
}
.region-dropdown {
  padding: 5px;
  border: 1px solid gray;
  border-radius: 6px;
  max-width: 200px;
  opacity: 0.6;
  margin-bottom: 7px;
}
</style>