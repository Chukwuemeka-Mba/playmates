<template lang="">
  <div class="flex-center body">
    <div class="signup">
      <h1>Signup</h1>
    </div>
    <div class="signup-form">
      <form @submit.prevent="submitForm">
        <div class="data">
          <label for="email">Email</label>
          <input type="email" name="email" v-model="email" />
        </div>
        <div class="data">
          <label for="username">Username</label>
          <input type="text" name="username" v-model="username" />
        </div>
        <div class="data">
          <label for="password">Password</label>
          <input type="text" name="password" v-model="password" />
        </div>
        <div class="data">
          <label for="password">Retype Password</label>
          <input type="text" name="password" v-model="password2" />
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
          <button type="submit" name="email">Signup</button>
        </div>

        <div class="data">
          <router-link to="/login">
            <p>Already have an account?</p></router-link
          >
        </div>
      </form>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import toast from "vue-toast-notification";
export default {
  name: "TheSignup",
  data() {
    return {
      email: "",
      username: "",
      password: "",
      password2: "",
      errors: [],
      isAuth: "",
    };
  },
  computed: {},
  methods: {
    submitForm() {
      this.errors = [];
      if (this.username === "") {
        this.errors.push("Your username is missing");
      } else if (this.password === "") {
        this.errors.push("The password is too short");
      } else if (this.password !== this.password2) {
        this.errors.push("The password doesn't match");
      }
      if (!this.errors.length) {
        const formData = {
          username: this.username,
          password: this.password,
        };
        axios
          .post("playmates-api/users/", formData)
          .then((response) => {
            toast({
              message: "Account created, please log in!",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });

            this.$router.push("/login");
            return response;
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(
                  `${property}: ${error.response.data[property]}`
                );
              }
              console.log(JSON.stringify(error.response.data));
            } else if (error.message) {
              this.errors.push("Something went wrong. Please try again");
              console.log(JSON.stringify(error));
            }
          });
      }
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
    url("../assets/signup.png");
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
