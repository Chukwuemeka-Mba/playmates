<template lang="">
  <section>
    <form>
      <label for="playmate">NEW PLAYMATE</label>
      <input type="text" name="playmate" required v-model="name" />

      <label for="playmate">Age</label>
      <input type="number" name="playmate" v-model="age" />

      <label for="playmate">Description</label>
      <input type="text" v-model="description" name="playmate" />

      <label for="playmate">Play Count</label>
      <input type="number" name="playmate" v-model="playCount" />

      <label for="playmate">Image</label>
      <input
        type="file"
        accept="image/*"
        name="playmate"
        value=""
        @change="updatePhoto($event.target.name, $event.target.files)"
      />

      <button type="submit">create new entry</button>
    </form>
  </section>
</template>
<script>
import axios from "axios";
export default {
  data() {
    return {
      name: "Whos the new mate 🥰?",
      age: "",
      description: "",
      playCount: "",
      image: {},
      rating: "",
      errorMessage: [],
    };
  },
  mounted() {
    document.title = "New Playmate | Playmates";
  },
  methods: {
    updatePhoto(files) {
      if (!files.length) return;

      // Store the file data
      this.image = {
        name: files[0].name,
        data: files[0],
      };
    },
    async addPlaymate() {
      const newPlaymate = {
        name: this.name,
        age: this.age,
        description: this.description,
        playCount: this.playCount,
        image: this.image,
      };
      await axios
        .post("http://127.0.0.1:8000/playmates-api/playmates/", newPlaymate)
        .then((res) => {
          this.newPlaymate = res.data.id;
          const token = res.data.auth_token;
          this.$store.commit("setToken", token);
          axios.defaults.headers.common["Authorization"] = "Token" + token;
          localStorage.setItem("token", token);

          this.$router.push("/archives");
          return res;
        })
        .catch((error) => {
          (this.errorMessage = error.message),
            console.error(
              "Could not add new Playmate. Please try again.",
              error
            );
        });
    },
  },
};
</script>
<style lang="scss" scoped>
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
