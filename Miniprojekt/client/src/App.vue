<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg bg-light navbar-light">
  <router-link class="navbar-brand" to="/">GastroLiter</router-link>
  <button class="navbar-toggler" v-bind="show ? 'collapsed' : ''"
  type="button" data-toggle="collapse" @click="toggleNavbar">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div v-bind:class="show ? 'show navbar-collapse collapse' : 'collapse navbar-collapse'"
  id="collapsibleNavbar">
    <ul class="navbar-nav">
      <li class="nav-item">
        <router-link class="nav-link" to="/">Home</router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link" to="/about">About</router-link>
      </li>
    </ul>
  </div>
</nav>
    <router-view />
  </div>
</template>

<script>
export default {
  data() {
    return {
      show: false,
    };
  },
  methods: {
    toggleNavbar() {
      this.show = !this.show;
    },
  },
};
</script>

<style>
body {
  height: 100vh;
}
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: 100%;
  padding: 0;

}
</style>
