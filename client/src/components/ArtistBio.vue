<template>
  <section class="bio">
    <div class='picture-cont'>
      <img :src="picture" alt="">
    </div>

    <div class=bio-cont>
      <button @click='goHome'>Home</button>
      <h3>{{name}}</h3>
      <h5>Bio: {{bio}}</h5>
    </div>

  </section>
</template>

<script>

export default {
  name: 'ArtistBio',
  props: {
    name: String,
    picture: String,
    bio: String
  },
  methods: {
    goHome() {
      this.$router.push('/')
    }
  }
}
</script>

<style scoped>
</style>