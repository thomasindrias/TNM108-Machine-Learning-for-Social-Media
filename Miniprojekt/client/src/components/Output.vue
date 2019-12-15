<template>
<div class="animated fadeIn">
<div class="overflow-auto box">
  <b-card-text>
    {{ msg }}
  </b-card-text>
</div>
<button type="button" @click="emitBack" class="mt-4 btn btn-primary btn-md">Retry?</button>
</div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Output',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    emitBack() {
      this.msg = '';
      this.$emit('retry', false);
    },
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
          // console.log(res);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
</script>

<style scoped>
.card {
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 14px 28px rgba(0, 0, 0, .25), 0 10px 10px rgba(0, 0, 0, .22);
    position: relative;
    overflow: hidden;
    width: 720px;
    max-width: 100%;
    padding: 5vw;
    height: 360px;
}

.box{
  height: 150px;
}

</style>
