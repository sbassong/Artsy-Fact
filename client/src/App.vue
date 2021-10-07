<template>
  <div id='app'> 
    <main class='main'>
      <ArtistList />
      <About />
      <router-view></router-view>
    </main>
  </div>
  
</template>

<script>
import ArtistList from './pages/ArtistsList.vue'
import About from './pages/About.vue'
export default {
  name: 'App',
  components: {
    ArtistList,
    About
  }
}
</script>

<style>

</style>
