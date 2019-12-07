<template>
  <div class="card flex">

  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Input',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
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

<style>
.card {
    background: #fff;
    border-radius: 10px;
    box-shadow: 0 14px 28px rgba(0, 0, 0, .25), 0 10px 10px rgba(0, 0, 0, .22);
    position: relative;
    overflow: hidden;
    width: 720px;
    max-width: 100%;
    height: 360px;
}
</style>
