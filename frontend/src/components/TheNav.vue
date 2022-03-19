<template lang="">
  <div>
    <nav>
      <div class="logo">
        <router-link to="/">
          <img src="../assets/p.svg" alt="logo" width="40" height="40" />
          <h1></h1
        ></router-link>
      </div>
      <div class="searchbar">
        <input type="search" name="searchbar" value="looking for something?" />
      </div>
      <div class="links" v-if="$store.state.isAuthenticated">
        <router-link to="/favorites" class="">Favorites </router-link>
        <router-link to="/archives" class=""> Archives</router-link>
        <router-link to="/account">
          <p>User: Logged in</p>
        </router-link>
      </div>
    </nav>
  </div>
</template>
<script>
export default {
  name: "TheNav",
};
</script>
<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap");
nav {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  padding: 10px 20px;
  max-height: 90px;
  background-color: #000000;
  font-family: "Roboto", sans-serif;
  box-shadow: 1px 2px 13px #868686;
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

    // //* Hamburger Style:
    // @media screen and (max-width: 700px) {
    //   display: none;
    // }
    label {
      color: #ff5a60;
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

@media screen and (max-width: 700px) {
  .searchbar input {
    display: none;
  }
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

// @media screen and(max-width: 720px) {
//   input {
//     display: none;
//   }
// }

nav svg {
  height: 30px;
  margin: 0px 10px;
}

.logo a {
  display: flex;
  flex-direction: row;
  align-items: center;
}
</style>
