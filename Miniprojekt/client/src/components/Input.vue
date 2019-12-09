<template>
  <div class="card flex">
<div class="form-group shadow-textarea">
  <form class="input md-form mb-4 pink-textarea active-pink-textarea"
      method="post" @submit.prevent="submit" >
    <label for="exampleFormControlTextarea6">Shadow and placeholder</label>
    <textarea class="form-control z-depth-1" id="exampleFormControlTextarea6"
    rows="3" placeholder="Write something here..."
    name="name" value="value" v-model="data"></textarea>
    <button type="submit" class="btn btn-success btn-sm" name="button">Summarize it!</button>
   </form>
</div>
    <!--
    <div class="form-group">
      <form class="input md-form mb-4 pink-textarea active-pink-textarea"
      method="post" @submit.prevent="submit" >
        <textarea name="name" class="md-textarea form-control" id="form18"
        value="value" v-model="data" cols="3" rows="10"></textarea>
        <label for="form18">Material textarea colorful on :focus state</label>
        <button type="submit" class="btn btn-success btn-sm" name="button">Summarize it!</button>
      </form>
    </div>
    -->
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Input',
  data() {
    return {
      data: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/ping';
      axios.get(path)
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
      axios.post(path, { data: this.data })
        // eslint-disable-next-line no-unused-vars
        .then((res) => {
          // eslint-disable-next-line no-console
          console.log(this.data);
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
.shadow-textarea textarea.form-control::placeholder {
    font-weight: 300;
}
.shadow-textarea textarea.form-control {
    padding-left: 0.8rem;
}
</style>
