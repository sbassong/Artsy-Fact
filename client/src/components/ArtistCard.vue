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