<template>
  <div>

    <div class="artists" v-if='searched' hidden>
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

export default {
  name: 'ArtistsList',
  components: {
    ArtistCard
  },
  data: () => ({
    artists: []
  }),
  mounted() {

  },
  methods: {
    async getArtists() {
      
    }
  }
}
</script>
