<template lang="html">
  <div class="body">
    <section>
      <div class="card">
        <div class="image-container">
          <img :src="playmate.image" />
        </div>

        <div class="card-text">
          <h1>{{ playmate.name }}</h1>
          <h2>AGE: {{ playmate.age }}</h2>
          <p>{{ playmate.description }}</p>
          <p>{{ playmate.rating }}</p>
          <p>{{ playmate.playcount }}</p>
          <p>{{ playmate.created_at }}</p>
        </div>
        <button type="">Add to Favorites</button>
      </div>
    </section>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "PlaymateDetail",
  props: {
    playmateId: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      playmate: {},
    };
  },
  mounted() {
    this.getPlaymate();
  },
  methods: {
    getPlaymate() {
      const id = this.$route.params.id;
      axios
        .get(`http://localhost:8000/playmates-api/playmates/${id}/`)
        .then((response) => {
          this.playmate = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    addToFavorites() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }
      const item = {
        playmate: this.playmate,
        quantity: this.quantity,
      };
      this.$store.commit("addToFavorites", item);
    },
  },
};
</script>
<style lang="scss" scoped>
.card {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin: 20px;
  padding: 10px;
  box-shadow: 1px 2px 13px rgb(221, 221, 221);
  overflow: hidden;
}

.image-container {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  img {
    position: relative;
    width: 100%;
    height: 20em;
    overflow: hidden;
  }
}
section {
  height: 100vh;
}

.card-text {
  display: flex;
  flex-direction: column;
  justify-content: center;
  // align-items: center;
  text-align: start;
  width: 100%;
  padding: 10px 20px;
  h1 {
    font-size: 16px;
  }
  h2 {
    font-size: 15px;
  }
}
</style>
