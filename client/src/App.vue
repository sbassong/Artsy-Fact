<template>
  <div id='app'> 
    <main class='main'>
    <Nav />
      <router-view></router-view>
    </main>
  </div>
  
</template>

<script>
import Nav from './components/Nav.vue'
export default {
  name: 'App',
  components:{
    Nav
  }
}
</script>

<style>
background{ 
position: absolute;
width: 100%;
height:100%;
}
</style>
