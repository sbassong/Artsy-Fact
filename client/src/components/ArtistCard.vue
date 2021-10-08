<template>
  <div class="card artist-card" >
    <div class="image-cont">
      <img :src='picture' alt="">
    </div>
    <div class="info-cont flex-col">
      <h3>{{name}}</h3>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ArtistCard',
  props: {
    name: String,
    picture: String
  }
}
</script>

<style scoped>
  .card {
  max-width: 300px;
  max-height: 380px;
  border-radius: 4px;
  background-color: #1b1b1b;
  cursor: pointer;
  transition: all 0.2s;
  margin: 0.5em
}

.card:hover {
  opacity: 0.8;
}

.card .image-cont {
  width: auto;
}

.card img {
  width: 100%;
  height: 200px;
}

.card .info-cont {
  padding: 1em;
}
</style>