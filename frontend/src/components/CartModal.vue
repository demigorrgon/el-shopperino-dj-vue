<template>
  <div class="modal-cart">
    <div class="modal-content">
      <vs-row>
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
      <p>Cart I guess</p>
    </div>
  </div>
</template>

<script>
export default {
  methods: {
    toggleCart() {
      this.$emit("closeCart");
    },
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