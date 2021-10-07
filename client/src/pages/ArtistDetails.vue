<template>
  <div class="artist-content">
    <ArtistBio />
    <Forum />
  </div>
</template>

<script>
  import Forum from '../components/Forum'
  import ArtistBio from '../components/ArtistBio'

export default {
  name: 'ArtistDetails',
  data: () => ({
    ArtistDetails: null,
    posts: []
  }),
  components: {
    Forum,
    ArtistBio
  },
  mounted() {
    this.getArtistDetails()
    this.getPosts()
  },
  methods: {
    async getArtistDetails() {
      // Get game id from router here
      
    },
    goHome() {
      this.$router.push('/')
    },
    async getPosts() {
      
    }
  }
}
</script>

<style scoped>
  .post {
    background-color: rgb(100, 97, 97);
    padding: .5em 1em;
    margin: 0.5em auto;
    border-radius: 20px
  }

  .post img,h6 {
    display: inline-block;
  }

  .img-cont {
    display: flex;
  }

  .img-cont div {
    margin: 1em ;
  }
</style>