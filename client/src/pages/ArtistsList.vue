<template>
  <div>

<<<<<<< HEAD
    <div class="artists" >
=======
    <div class="artists">
>>>>>>> 2a9efd9aaf73480fc7de03f34113135e1c6d287d
      <h2>Artists</h2>
      <section class="container-grid" v-for='artist in artists' :key='artist.id'>
        <div @click="selectArtist(artist.id)">
          <ArtistCard :picture='artist.picture' :name='artist.name' />
        </div>
      </section>
    </div>

  </div>
</template>

<script>
import {GetArtists} from '../services/artists'
import ArtistCard from '../components/ArtistCard.vue'

export default {
  name: 'ArtistsList',
  components: {
    ArtistCard
  },
  data: () => ({
    artists: []
  }),
  mounted() {
    this.getArtists()
  },
  methods: {
    async getArtists() {
      const artists = await GetArtists()
      this.artists = artists
    },
    selectArtist(artist_id) {
      this.$router.push(`/artists/details/${artist_id}`)
    }
  }
}
</script>
