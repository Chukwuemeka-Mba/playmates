<template>
  <div class="home">
    <h1>Your dating experiences, <br />all in one place.</h1>
    <section>
      <router-link to=""> <button>Try playmates for Free</button> </router-link>
    </section>
    <section></section>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "HomeView",
  components: {},
};
</script>

<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Raleway&display=swap");

.home {
  display: flex;
  flex-direction: column;
  text-align: center;
  background-image: url("../assets/home.png");
  background-position: center;
  background-size: 800px;
  background-repeat: no-repeat;
  background-position-y: 20px;
  height: 100vh;
  h1 {
    margin: 200px 0px;
    color: #000000;
    font-weight: 700px;
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
