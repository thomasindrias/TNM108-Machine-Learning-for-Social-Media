<template>
  <div class="container">
    <div class="column bg-primary half-box">
       <b-img src="https://www.shareicon.net/data/512x512/2016/10/22/846922_book_512x512.png"
      class="logo m-3" rounded fluid alt="Responsive image"></b-img>
      <b-jumbotron
        class="p-0 text-white"
        header="GastroLiter"
        lead="A miniproject for the course TNM108 at LiU"
        bg-variant=transparent>
      </b-jumbotron>
      <div class="row half-box"></div>
      <b-card
      v-bind:title="!inputStatus ? 'Paste your ' + data_type +' review below!': 'Summarized!'"
          class="card animated bounceInUp">
        <Input v-if="!inputStatus" @submit="inputData" @radio="dataUpdate"/>
        <Output v-else @retry="inputData"/>
      </b-card>
    </div>
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
      data_type: '',
    };
  },
  methods: {
    inputData(status) {
      this.inputStatus = status;
    },
    dataUpdate(type) {
      this.data_type = type;
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

textarea {
  resize:none;
}

.half-box{
    height: 50%;
    width: 100vw;
    padding: 0;
}
.half-box-header{
    height: 50%;
    max-width: 20rem;
    padding: 10;
}

.card {
  position: absolute;
  left: calc(50vw - 360px);
  top: calc(50vh - 80px);
  z-index: 1;
}

.logo {
  height: 100px;
}
</style>
