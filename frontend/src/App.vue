<template>
  <div>
    <nav-bar></nav-bar>
    <router-view />
    <footer-bar></footer-bar>
  </div>
</template>

<script>
import NavBar from "./components/NavBar.vue";
import FooterBar from "./components/FooterBar.vue";

export default {
  components: {
    NavBar,
    FooterBar,
  },
  data() {
    return {};
  },
};
</script>
<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #000000;
  height: 100vh;
}

body {
  margin: 0px;
  background-image: url("./assets/datingimg.jpeg");
}
</style>
