<template>
  <div id='app'> 
    <main class='main'>
      <Nav />
      <router-view></router-view>
    </main>
  </div>
  
</template>

<script>
import nav from './components/Nav'
export default {
  name: 'App',
  components: {
  Nav
  }
}
</script>

<style>
/* background{ 
position: absolute;
width: 1013px;
height: 662px;
} */
</style>
