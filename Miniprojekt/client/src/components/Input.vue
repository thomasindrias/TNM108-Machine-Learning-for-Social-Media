<template>
    <div class="form-group shadow-textarea">
      <form class="input md-form mb-4 pink-textarea active-pink-textarea"
          method="post" @submit.prevent="submit" >
        <label for="exampleFormControlTextarea6"
        class="text-danger animated shake delay-2s">{{ error }}</label>
        <textarea class="form-control z-depth-1" id="exampleFormControlTextarea6"
        rows="3" placeholder="Paste your review here..."
        name="name" value="value" v-model="data"></textarea>
        <div class="mt-3">
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio"
            name="exampleRadios" id="book" v-model="data_type"
            v-bind:value="'book'" v-on:change="data_type_set" checked>
            <label class="form-check-label" for="book">
              Book
            </label>
          </div>
          <div class="form-check form-check-inline">
            <input class="form-check-input" type="radio"
            name="exampleRadios" id="food" v-model="data_type"
            v-bind:value="'food'" v-on:change="data_type_set">
            <label class="form-check-label" for="food">
              Food
            </label>
          </div>
        </div>
        <button type="submit" class="mt-3 btn btn-primary btn-md"
        name="button">Summarize it!</button>
      </form>
    </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Input',
  data() {
    return {
      data: '',
      error: '',
      data_type: 'book',
    };
  },
  mounted() {
    this.data_type_set();
  },
  methods: {
    data_type_set() {
      this.$emit('radio', this.data_type);
    },

    async submit() {
      this.error = '';

      // Check if text is long enough
      if (this.data.length < 10) {
        this.error = 'Enter a longer review.';
        return;
      }

      const path = 'http://localhost:5000/ping';
      let status = false;
      await axios.post(path, { data: this.data, data_type: this.data_type })
        // eslint-disable-next-line no-unused-vars
        .then((res) => {
          // eslint-disable-next-line no-console
          // console.log(this.data);
          status = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
        });
      await this.$emit('submit', status);
    },
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
    padding-left: 3vw;
    padding-right: 3vw;
}
.shadow-textarea textarea.form-control::placeholder {
    font-weight: 300;
}
.shadow-textarea textarea.form-control {
    padding-left: 0.8rem;
}
</style>
