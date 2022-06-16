<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <!-- <div class="modal-header">
            <slot name="header">  </slot>
          </div> -->

          <vs-row class="modal-body">
            <vs-col vs-offset="12" vs-align="flex-end" vs-justify="flex-end">
              <vs-button
                class="modal-default-button"
                color="danger"
                type="border"
                @click="$emit('close')"
                icon="close"
                style="transform: scale(0.65)"
              >
              </vs-button>
            </vs-col>
          </vs-row>
          <vs-row>
            <vs-col name="body">
              <b
                >Please <a href="/login" class="reroute-link">login</a> or
                <a href="/register" class="reroute-link">register</a> to submit
                your order</b
              >
            </vs-col>
          </vs-row>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  methods: {
    closeModal() {
      this.$emit("close");
    },
  },
};
</script>

<style scoped>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 0px 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  /* margin: 20px 0; */
}

.modal-default-button {
  float: right;
}
.reroute-link {
  text-decoration: underline;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>