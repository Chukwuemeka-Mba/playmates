<template lang="">
  <div class="playmate">
    <div class="card">
      <div class="card-text">
        <h1>Playmate</h1>
        <p>What went down?</p>
        <p>Date | Location</p>
      </div>
      <div class="card-img"></div>
    </div>
  </div>
</template>
<script>
export default {
  name: "PlaymateCard",
};
</script>
<style lang="scss" scoped>
.card {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  background-color: white;
  border-radius: 5px;
  width: 100%;
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
  background-image: url("../assets/datingimg.jpeg");
  background-position: center;
  min-width: 25em;
  border-radius: 5px;
}
</style>
