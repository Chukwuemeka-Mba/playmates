<template lang="">
  <div class="playmate">
    <div class="card">
      <div class="card-img">
        <img :src="playmate.image" alt="" />
      </div>
      <div>
        <div class="card-text">
          <div class="title">
            <h1>
              {{ playmate.name }}
            </h1>
            <div>
              <font-awesome-icon :icon="['fas', 'heart-circle-plus']" />
            </div>
          </div>
          <p>{{ playmate.description }}</p>
          <p>{{ playmate.age }} years | {{ playmate.rating }} stars</p>
        </div>
        <div class="button">
          <router-link :to="{ name: 'playmate', params: { id: playmate.id } }">
            <button type="">View Details</button></router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "PlaymateCard",
  props: {
    playmate: {
      type: Object,
      default: () => {},
    },
    data() {
      return {
        // router: this.$route.params.id,
      };
    },
  },
};
</script>
<style lang="scss" scoped>
.card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: white;
  border-radius: 15px;
  width: 90%;
  margin: 20px;
  box-shadow: 0px 5px 10px gray;
}

.card-text {
  display: flex;
  flex-wrap: wrap;
  justify-content: flex-start;
  align-items: start;
  flex-direction: column;
  padding: 0px 30px;
  // width: 300px;
  p {
    max-width: 350px;
    font-size: 13px;
  }
  h1 {
    font-size: 20px;
  }
}

.card-img {
  display: flex;
  flex-direction: column;
}

.card-img img {
  width: 200px;
  height: 200px;
  margin-top: 50px;
  margin-left: 20px;
}

.button {
  display: flex;
  justify-content: center;
}
button {
  background-color: #ff5a60;
  padding: 7px 20px;
  margin: 20px;
  color: #ffffff;
  border-radius: 20px;
  border: 0px;
}

@media screen and (min-width: 700px) {
  .card {
    display: flex;
    flex-direction: row;
    width: 100%;
  }
  .card-img {
    height: 295px;
    width: 70%;
  }
}
.title {
  display: flex;
  align-items: center;
  gap: 100%;
  svg {
    height: 20px;
    color: #f65653;
  }
}
</style>
