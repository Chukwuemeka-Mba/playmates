<template>
  <div class="archives">
    <div class="title">
      <h1>All archives</h1>
      <h2>Play Count: {{ bodyCount }}</h2>
    </div>
    <div class="cards">
      <playmate-card
        v-for="playmate in playmates"
        :key="playmate.id"
        :playmate="playmate"
      ></playmate-card>
    </div>
  </div>
</template>

<script>
import PlaymateCard from "../components/PlaymateCard.vue";
import axios from "axios";
export default {
  name: "TheArchives",
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
    document.title = "Archives | Playmates";
  },
  methods: {
    getPlaymates() {
      axios.get("playmates-api/playmates/").then((response) => {
        this.playmates = response.data;
        this.bodyCount = this.playmates.length;
      });
    },
    getPlaymateDetail(num) {
      this.$router.push({
        name: "playmate",
        params: { playmateId: num },
      });
    },
  },
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap");
.archives {
  font-family: "Roboto", "sans-serif";
}
.title {
  display: flex;
  justify-content: space-between;
  margin: 10px 30px;
  font-size: 10px;
  font-weight: normal;
}
.cards {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 20px;
}
@media (min-width: 20em) and (max-width: 35em) {
  .cards {
    display: grid;
    grid-template-columns: repeat(1, 1fr);
  }
}

@media screen and (min-width: 900px) {
  .cards {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
  }
}
</style>
