<template lang="">
  <div v-for="favorites in favorites">
    <playmate-card
      v-for="playmate in playmates"
      :key="playmate.id"
      :playmate="playmate"
    ></playmate-card>
  </div>
</template>
<script>
import { mapState } from "vuex";
export default {
  name: "TheFavorites",
  data() {
    return {
      favorites: favorites,
      playmates: "",
    };
  },
  computed: {
    ...mapState(["favorites"]),
  },
};
</script>
<style lang=""></style>
