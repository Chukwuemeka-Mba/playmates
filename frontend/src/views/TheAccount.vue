<template lang="">
  <div class="account-body">
    <div class="head">
      <div>
        <img src="../assets/user.jpeg" width="190" height="190" />
      </div>
      <div class="account-info">
        <h1>Claire</h1>
        <p>
          Manage your info, privacy and security to make Playmates work better
          for you.
        </p>
      </div>
    </div>
    <div class="body">
      <div class="card">
        <div class="text-box">
          <div class="text-info">
            <h1>Personal Information</h1>
            <p>
              See the data in your Account. Personalise your Playmates
              experience
            </p>
          </div>
          <div class="">
            <img src="../assets/privacy.webp" alt="" width="350" />
          </div>
        </div>
        <div class="link">
          <router-link to="">Edit details</router-link>
        </div>
      </div>
      <div class="card">
        <div class="text-box">
          <div class="text-info">
            <h1>Subscriber Information</h1>
            <p>
              Choose between top tier plans.
              <br />
              <strong> Gold | Diamond | Platinum</strong>
            </p>
          </div>
          <div class="">
            <img src="../assets/payments.webp" alt="" width="350" />
          </div>
        </div>
        <div class="link2">
          <router-link to="">Pay with Stripe</router-link>
        </div>
      </div>
    </div>
    <div class="info">
      <div class="danger-card">
        <div class="danger">
          <h2>Danger Zone</h2>
          <p>Are you sure you want to go here?</p>
        </div>
        <div class="text-box danger-btn">
          <div class="logout">
            <router-link to="">Log Out</router-link>
          </div>
          <div class="delete-account">
            <router-link to="">Delete Account</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {};
</script>
<style lang="scss">
//* Mixins

@mixin flex-enter {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
@mixin flex-row {
  display: flex;
  flex-direction: row;
  justify-content: start;
  align-items: center;
}
.account-body {
  display: grid;
  grid-template-columns: 1fr;
  grid-template-rows: 0.2fr 1fr 0.8fr;
  grid-template-areas:
    "head"
    "body"
    "info";
}

.head {
  grid-area: head;
  @include flex-enter();
  img {
    border-radius: 100%;
    margin-top: 20px;
  }
}
.body {
  grid-area: body;
  //   background-color: #5146b8;
  padding: 20px;
}

.info {
  @include flex-enter();
  grid-area: info;

  .danger {
    @include flex-enter();
    margin: 100px 0px;
  }

  .danger h2 {
    color: #db080f;
    padding-left: 40px;
    font-size: 40px;
    width: 300px;
    align-items: center;
    border-radius: 20px;
  }
  .danger p:hover {
    color: #db080f;
  }
  .danger-btn {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    .logout a {
      text-decoration: none;
      padding: 10px 50px;
      background-color: rgb(190, 190, 190);
      color: #fff;
      border-radius: 20px;
    }
    .delete-account a {
      text-decoration: none;
      padding: 10px 50px;
      background-color: rgb(233, 45, 45);
      color: #fff;
      border-radius: 20px;
    }
  }
}

@media screen and (min-width: "700px") {
  .account-body {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-template-rows: 0.3fr 0.6fr 0.4fr;
    grid-template-areas:
      "head head head"
      "body body body"
      "info info info";
  }
  .body {
    display: flex;
    flex-direction: row;
  }
}
.account-info {
  @include flex-enter();
  text-align: center;
  p {
    font-size: 20px;
    width: 70%;
    color: rgb(155, 155, 155);
  }
  .danger {
    @include flex-enter();
    margin: 100px 0px;
  }
}

.text-box {
  @include flex-row();
  .text-info {
    max-width: 300px;
  }
}
.card {
  box-shadow: 1px 7px 24px rgb(201, 199, 200);
  margin: 20px;
  padding: 20px;
  border-radius: 20px;
}
.link a {
  background-color: #ff5a60;
  padding: 10px 20px;
  margin: 20px 30px;
  border-radius: 10px;
  text-decoration: none;
  color: #fff;
}
.link2 a {
  background-color: rgb(100, 187, 228);
  padding: 10px 20px;
  margin: 20px 30px;
  border-radius: 10px;
  text-decoration: none;
  color: #fff;
}
</style>
