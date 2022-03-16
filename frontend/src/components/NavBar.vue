<template lang="">
  <div>
    <nav>
      <div>
        <router-link to="/"><h1>Playmates</h1></router-link>
      </div>
      <div class="links">
        <router-link to="/">Home</router-link>
        <router-link to="/archives" class="archives">Archives</router-link>
        <router-link to=""></router-link>
      </div>
    </nav>
  </div>
</template>
<script>
export default {
  name: "NavBar",
};
</script>
<style lang="scss" scoped>
nav {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 0px 20px;
  max-height: 90px;
  a,
  h1 {
    color: #ff5a60;
  }
  a {
    text-decoration: none;
    font-weight: bold;
  }
  .links {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    gap: 10px;
  }
}

.archives {
  background-color: #ff5a60;
  color: #ffffff;
  padding: 5px 10px;
  border-radius: 10px;
}

img {
  width: 60px;
  height: 60px;
  border-radius: 100%;
}
</style>
