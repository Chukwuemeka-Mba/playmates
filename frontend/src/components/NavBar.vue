<template lang="">
  <div>
    <nav>
      <div>
        <router-link to="/"><h1>Playmates</h1></router-link>
      </div>
      <div class="searchbar">
        <input type="search" name="searchbar" value="looking for something?" />
      </div>
      <div class="links">
        <router-link to="/" class="">Home</router-link>
        <router-link to="/favorites" class="">Favorites</router-link>
        <router-link to="/archives" class="">Archives</router-link>
        <router-link to="/account">
          <div class="account-icon">
            <img src="../assets/playboy.jpeg" alt="" />
          </div>
        </router-link>
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
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap");
nav {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 0px 20px;
  max-height: 90px;
  background-color: #ffffff;
  font-family: "Roboto", sans-serif;
  box-shadow: 1px 2px 3px #e5e5e5;
  border-radius: 25px;
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
    a:hover {
      text-decoration: underline 1px #ff5a60;
    }
  }
}

.archives {
  background-color: #ff5a60;
  color: #ffffff;
  padding: 5px 10px;
  border-radius: 10px;
}

.account-icon img {
  width: 45px;
  height: 45px;
  border-radius: 20px;
  border: 1px solid #9e9e9e;
}

.searchbar input {
  width: 400px;
  height: 40px;
  border-radius: 30px;
  padding: 15px 20px;
  border: 0.5px solid #ff5a60;
}
input:hover {
  border: 0.5px solid #11366e;
}

@media screen and(max-width: 720px) {
  input {
    display: none;
  }
}
</style>
