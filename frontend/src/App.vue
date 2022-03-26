<template>
  <div>
    <the-nav></the-nav>
  </div>

  <router-view v-slot="{ Component }">
    <transition name="route" mode="out-in">
      <component :is="Component"></component>
    </transition>
  </router-view>
</template>

<script>
import TheNav from "./components/TheNav.vue";
// import axios from "axios";

export default {
  name: "App",
  components: {
    TheNav,
    // FooterBar,
  },
  data() {
    return {
      favorites: "",
    };
  },
  // beforeCreate() {
  //   this.$store.commit("initializeStore");
  //   const token = this.$store.state.token;
  //   if (token) {
  //     axios.defaults.headers.common["Authorization"] = "Token " + token;
  //   } else {
  //     axios.defaults.headers.common["Authorization"] = "";
  //   }
  // },
  mounted() {
    this.cart = this.$store.state.favorites;
  },
  computed: {},
};
</script>
<style lang="scss">
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@300&display=swap");

body {
  margin: 0px;
  // background-image: url("./assets/datingimg.jpeg");
  background-position: center;
  font-family: "Roboto", sans-serif;
}

//* Route Transitions

.router-enter-from {
  opacity: 0;
  transform: translateX();
}

.route-enter-active {
  transition: all 0.1s ease-out;
}

.route-leave-to {
  opacity: 0;
  transform: all 0.1s ease-out;
}

.route-leave-active {
  transition: all 0.1s ease-in;
}
</style>
