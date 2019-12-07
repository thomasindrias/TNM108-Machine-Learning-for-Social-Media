<template>
<div class="container">
  <div class="row bg-primary half-box">
  </div>
    <div class="row half-box">
  </div>
  <Input class="card"/>
</div>
</template>

<script>
import Input from '../components/Input.vue';

export default {
  name: 'Home',
  components: {
    Input,
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
