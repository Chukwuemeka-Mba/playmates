<template>
  <div class="archives">
    <div class="title">
      <h1>All archives</h1>
      <h2>Body Count: {{ bodyCount }}</h2>
    </div>
    <div class="cards" :v-for="playmate in playmates">
      <playmate-card :playmate="playmate"></playmate-card>
    </div>
  </div>
</template>

<script>
import PlaymateCard from "../components/PlaymateCard.vue";
import axios from "axios";
export default {
  name: "ArchivesView",
  components: {
    PlaymateCard,
  },
  props: {
    playmate: Object,
  },
  data() {
    return {
      playmates: [],
      bodyCount: "",
    };
  },
  mounted() {
    this.getPlaymates();
  },
  methods: {
    getPlaymates() {
      axios.get("playmates-api/playmates/").then((response) => {
        this.playmates = response.data;
        console.log(this.playmates[0]);
      });
    },
    getBodyCount() {
      this.bodyCount = this.playmates.length;
      console.log(this.bodyCount);
    },
  },
};
</script>

<style lang="scss" scoped>
.archives {
  background-color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
  font-size: 10px;
  height: 100vh;
  .title {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 300px;
  }
}
.cards {
  display: flex;
  flex-direction: column;
  margin: 20px 20px;
}
</style>
