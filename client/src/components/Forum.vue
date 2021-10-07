<template>
  <div class="forum">

    <section class="post-form-cont">
      <button class='show-form-button' @click='renderForm'>Add</button>
      <PostForm :artist_id='artist_id' v-if='clicked'/>
    </section>

    <section class="posts">
        <h3>Posts</h3>
      <div>
        <section v-for='post in posts' :key='post.id'>
          <div class="post">
            <h4>Reviewer: {{post.reviewer}}</h4>
            <h5>{{post.content}}</h5>
          </div>
        </section>
      </div>
      
      
    </section>
  </div>
</template>

<script>
import PostForm from './PostForm.vue'

export default {
  name: 'Forum',
  data: () => ({
  }),
  components: {
    PostForm
  },
  props: {
    posts: Array
  },
  methods: {

  }
}
</script>

<style scoped>
  .post {
    /* background-color: rgb(100, 97, 97); */
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