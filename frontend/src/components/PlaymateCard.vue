<template lang="">
  <div class="playmate">
    <div class="card">
      <div class="card-img">
        <img :src="playmate.image" alt="" />
      </div>
      <div class="card-text">
        <h1>{{ playmate.name }}</h1>
        <p>{{ playmate.description }}</p>
        <p>{{ playmate.age }} years | {{ playmate.rating }} stars</p>
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
  },
};
</script>
<style lang="scss" scoped>
.card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: white;
  border-radius: 5px;
  width: 100%;
  max-width: 250px;
  box-shadow: 0px 5px 10px gray;
}

.card-text {
  display: flex;
  flex-direction: column;
  padding: 10px 20px;
  width: 100%;
}

.card-img {
  display: flex;
  flex-direction: column;
  background-position: center;
  height: 20em;
}

.card-img img {
  height: 100%;
}

.playmate {
  display: grid;
  margin: 20px 0px;
  grid-template-columns: 1fr;
  grid-template-rows: 1fr;
}
</style>
