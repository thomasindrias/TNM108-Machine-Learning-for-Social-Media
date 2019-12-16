<template>
<div class="container">
  <div class="row bg-primary half-box">
  </div>
    <div class="row half-box">
  </div>
  <b-card v-bind:title="!inputStatus ? 'Paste your text below!': 'Summarized!'"
  class="card animated bounceInUp">
  <Input v-if="!inputStatus" @submit="inputData"/>
  <Output v-else @retry="inputData"/>
  </b-card>

</div>
</template>

<script>
import Input from '../components/Input.vue';
import Output from '../components/Output.vue';

export default {
  name: 'Home',
  components: {
    Input,
    Output,
  },
  data() {
    return {
      inputStatus: false,
    };
  },
  methods: {
    inputData(status) {
      this.inputStatus = status;
    },
  },
};
</script>

<style>
.container {
    height: 100vh;
    margin: 0;
    position: relative;
}

.half-box{
    height: 50%;
    width: 100vw;
    padding: 0;
}

.card {
  position: absolute;
  left: calc(50vw - 360px);
  top: calc(50vh - 180px);
}
</style>
