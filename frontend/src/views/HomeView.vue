<template>
  <div class="home">
    <h1>Your dating experiences, <br />all in one place.</h1>
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
.home {
  display: flex;
  flex-direction: column;
  text-align: center;
  h1 {
    margin: 200px 0px;
    color: white;
  }
}
</style>
