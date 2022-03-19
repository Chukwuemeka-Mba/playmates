<template lang="">
  <div class="flex-center body">
    <div class="signup">
      <h1>Login</h1>
    </div>
    <div class="signup-form">
      <form @submit.prevent="submitForm">
        <div class="data">
          <label for="username">Username</label>
          <input type="text" name="username" v-model="username" />
        </div>
        <div class="data">
          <label for="password">Password</label>
          <input type="text" name="password" v-model="password" />
        </div>
        <div class="data" v-if="errors.length">
          <div v-for="error in errors" :key="error">
            {{ error }}
          </div>
        </div>
        <div class="isAuth">
          <label for="email">Keep me logged in</label>
          <input type="checkbox" name="isAuth" v-model="isAuth" />
        </div>
        <div class="data">
          <button type="submit" name="email">Login</button>
        </div>
      </form>
      <div class="data">
        <router-link to="/login"> <p>Don't have an account?</p></router-link>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
export default {
  name: "TheLogin",
  data() {
    return {
      email: "",
      username: "",
      password: "",
      errors: [],
    };
  },
  computed: {},
  mounted() {
    document.title = "Login | Playmates";
  },
  methods: {
    async submitForm() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");

      const formData = {
        username: this.username,
        password: this.password,
      };
      await axios
        .post("playmates-api/token/login", formData)
        .then((response) => {
          const token = response.data.auth_token;
          this.$store.commit("setToken", token);
          axios.defaults.headers.common["Authorization"] = "Token" + token;
          localStorage.setItem("token", token);

          this.$router.push("/home");
          return response;
        })
        .catch((error) => {
          if (error.response) {
            for (const property in error.response.data) {
              this.errors.push(`${property}: ${error.response.data[property]}`);
            }
          } else {
            this.errors.push("Something went wrong. Please try again");
            console.log(JSON.stringify(error));
          }
        });
    },
  },
};
</script>
<style lang="scss" scoped>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@100&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@400&display=swap");

//* Sass Variables
$dark: #000;

//* Regular Sass Styles
.body {
  display: flex;
  flex-direction: column;
  text-align: center;
  height: 100vh;
  background: linear-gradient(
      rgba(255, 255, 255, 0.822),
      rgba(255, 255, 255, 0.5)
    ),
    url("../assets/login.png");
  background-position: center;
  background-size: 800px;
  background-repeat: no-repeat;
  background-position-y: 20px;
}

.signup {
  display: flex;
  justify-content: center;
  font-family: "Roboto", "sans serif";
  font-weight: 100;
  font-size: 20px;
}

.flex-center {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.signup-form {
  input {
    width: 250px;
    height: 35px;
    border-radius: 20px;
    padding: 1px 20px;
    border: 1px solid #83859c;
  }
  input:hover {
    border: 1px solid #ff5a60;
  }
  .data {
    display: flex;
    flex-direction: column;
    justify-content: start;
    margin: 2px;
    gap: 5px;
    color: #ff5a60;
    label {
      margin-left: 10px;
      margin-top: 10px;
    }
    button {
      margin: 10px 30px;
      padding: 10px 20px;
      border-radius: 10px;
      border: 1px solid #83859c;
      background-color: #ff5a60;
    }
    a {
      text-decoration: none;
      color: #0c3652;
    }
  }
  .isAuth {
    display: flex;
    align-items: center;
    margin-top: 10px;
    margin-left: 10px;

    input {
      width: 25px;
      border-radius: 20%;
      margin-left: 120px;
    }
  }
}
</style>
