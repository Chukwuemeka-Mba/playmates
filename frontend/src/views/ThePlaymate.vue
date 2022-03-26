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

      <div class="noted">
        <h1>Notes on Notes:</h1>
        <div class="add-note">
          <label for="playmate">New Note</label>
          <input type="text" name="playmate" value="Who's the new mate?" />
        </div>

        <div class="all-notes"></div>
      </div>
    </section>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "PlaymateDetail",
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
          document.title = this.playmate.name + " | Playmates";
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

section {
  // display: flex;
  // justify-content: center;
  // align-items: center;

  form {
    max-width: 420px;
    margin: 30px auto;
    background: white;
    text-align: left;
    padding: 40px;
    border-radius: 10px;
  }
  label {
    color: #aaa;
    display: inline-block;
    margin: 25px 0 15px;
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px;
    font-weight: bold;
  }
  input {
    display: block;
    padding: 10px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none;
    border-bottom: 1px solid #ddd;
    color: #555;
    //*
  }
  button {
    display: block;
    width: 150px;
    margin: 30px 0px auto;
    border-radius: 5px;
    border: 1px solid #ddd;
    padding: 5px 10px;
  }
}
</style>
