<template>
  <nav-bar></nav-bar>
  <router-view />
</template>

<script>
import NavBar from "./components/NavBar.vue";
// import FooterBar from "./components/FooterBar.vue";

export default {
  name: "App",
  components: {
    NavBar,
    // FooterBar,
  },
  data() {
    return {};
  },
};
</script>
<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@200&display=swap");

body {
  margin: 0px;
  // background-image: url("./assets/datingimg.jpeg");
  background-position: center;
  font-family: "Raleway", sans-serif;
}
</style>
