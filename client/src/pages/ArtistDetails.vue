<template>
  <div class="artist-content">
    <ArtistBio :name='artistDetails.name' :picture='artistDetails.picture' :bio='artistDetails.bio'/>
    <Forum :artist_id='artistDetails.id' />
  </div>
</template>

<script>
  import Forum from '../components/Forum'
  import ArtistBio from '../components/ArtistBio'

  import {GetArtistById} from '../services/artists'

export default {
  name: 'ArtistDetails',
  data: () => ({
    artistDetails: null,
  }),
  components: {
    Forum,
    ArtistBio
  },
  mounted() {
    this.getArtistDetails()
  },
  methods: {
    async getArtistDetails() {
      const artist_id = parseInt(this.$route.params.artist_id)

      const details = await GetArtistById(artist_id)
      this.artistDetails = details.data
    }
  }
}
</script>

<style scoped>

</style>