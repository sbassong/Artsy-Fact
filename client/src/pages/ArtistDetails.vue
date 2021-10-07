<template>
  <div class="artist-content">
    <ArtistBio :name='artistDetails.name' :picture='artistDetails.picture' :bio='artistDetails.bio'/>
    <Forum :artist_id='artistDetails.id'/>
  </div>
</template>

<script>
  import Forum from '../components/Forum'
  import ArtistBio from '../components/ArtistBio'

  import {GetArtistById} from '../services/artists'
  import {GetPostsByArtistId} from '../services/posts'

export default {
  name: 'ArtistDetails',
  data: () => ({
    artistDetails: null,
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
      const artist_id = parseInt(this.$route.params.artist_id)

      const details = await this.GetArtistById(artist_id)
      this.artistDetails = details.data
    },
    async getPosts() {
      const artist_id = parseInt(this.$route.params.artist_id)

      const posts = await this.GetPostsByArtistId(artist_id)
      this.posts = details.data
    }
  }
}
</script>

<style scoped>

</style>