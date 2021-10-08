<template>
  <div>

      <h2>Artists</h2>
    <div class="artists">
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

<style scoped>
  .artists {
    display: grid;
    grid-template: auto / repeat(4, 1fr);
    padding: 1em
  }

  h2 {
    text-align: center;
  }
</style>