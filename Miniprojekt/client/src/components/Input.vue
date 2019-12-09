<template>
  <div class="card flex">
    <div class="form-group">
      <form class="input" method="post" @submit.prevent="submit">
        <input type="text" name="name" value="value" v-model="name">
        <button type="submit" class="btn btn-success btn-sm" name="button">Summarize it!</button>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Input',
  data() {
    return {
      name: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      this.axios.get(path)
        .then((res) => {
          // console.table(res.data);
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    submit() {
      const path = 'http://localhost:5000/ping';
      this.axios.post(path, { name: this.name })
        .then(({ data }) => {
          // console.log(this.formValue);
          this.$emit('created', data);
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
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
    padding: 5vw;
    height: 360px;
}
</style>
