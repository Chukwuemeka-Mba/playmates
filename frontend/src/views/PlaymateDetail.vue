<template lang="html">
  <div class="container">
    <div>
      <img :src="playmate.img" />
      <div>
        <h1>Imagine this</h1>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "PlaymateDetail",
  props: {
    playmateId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      playmate: {},
    };
  },
  methods: {
    getPlaymate() {
      axios
        .get(`http://localhost:8000/playmates-api/playmates/${this.playmateId}`)
        .then((response) => {
          return (this.playmate = response.data);
        })
        .catch((error) => {
          console.log(error);
        });
      console.log(this.playmate);
    },
  },
};
</script>
<style lang="scss">
.container {
  background-color: #ffffff;
  height: 100vh;
}
</style>
