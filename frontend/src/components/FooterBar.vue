<template lang="">
  <div>
    <footer>
      <div class="support card">
        <h1>Support</h1>
        <div class="links">
          <router-link to="">Help Center</router-link>
          <router-link to="">Sefety Information</router-link>
          <router-link to="">Mental Health Support</router-link>
          <router-link to="">COVID-19</router-link>
        </div>
      </div>
      <div class="Com card">
        <h1>Community</h1>
        <div class="links">
          <router-link to="">Playmates.com</router-link>
          <router-link to="">Playmates of the Week</router-link>
        </div>
      </div>
      <div class="About card">
        <h1>About</h1>
        <div class="links">
          <router-link to="">Newsroom</router-link>
          <router-link to="">Learn about new Features</router-link>
          <router-link to="">Founders</router-link>
          <router-link to="">Investors</router-link>
          <router-link to="">Join the team</router-link>
        </div>
      </div>
    </footer>
  </div>
</template>
<script>
export default {
  name: "FooterBar",
};
</script>
<style lang="scss" scoped>
footer {
  position: fixed;
  bottom: 0px;
  display: flex;
  flex-direction: row;
  gap: 20px;
  justify-content: center;
  text-align: start;
  background-color: #000000;
  color: #ffffff;
  width: 100%;

  h1 {
    font-size: 20px;
  }

  .links {
    display: flex;
    flex-direction: column;
  }
  a {
    text-decoration: none;
    color: #ffffff;
    padding: 4px 5px;
  }
}
</style>
