<template>
  <div class="home">
    <h1>Your dating experiences, <br />all in one place.</h1>
    <section>
      <router-link to="/signup">
        <button>Try playmates for Free</button>
      </router-link>
    </section>
    <section></section>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "HomeView",
  components: {},
  data() {
    return {};
  },
  mounted() {
    document.title = "Home | Playmates";
  },
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Raleway&display=swap");

.home {
  display: flex;
  flex-direction: column;
  text-align: center;
  background: url("../assets/home.png");
  background-position: center;
  background-size: 100%;
  background-repeat: no-repeat;
  background-position-y: 200px;
  background-blend-mode: darken;
  height: 100vh;
  h1 {
    margin: 250px 0px;
    color: #000000;
    font-weight: 700px;
    font-size: 41px;
    line-height: 56px;
    letter-spacing: 1.6px;

    @media screen and(min-width: 700px) {
      width: 501;
      height: 155px;
      top: 125px;

      font-family: "Roboto";
      font-style: normal;
      font-weight: 700;
      font-size: 41px;
      line-height: 56px;
      letter-spacing: 1.6px;
    }
  }
}

button {
  padding: 10px 20px;
  background-color: #ff5a60;
  color: #ffffff;
  font-size: 17px;
  border-radius: 8px;
  border: 1px solid black;
}
</style>
