<template>
  <div class="forum">

    <section class="post-form-cont">
      <button class='show-form-button' @click='renderForm'></button>
      <PostForm v-if='clicked'/>
    </section>

    <section class="posts">
        <h3>Posts</h3>
      <div>
        <section v-for='post in posts' :key='post.id'>
          <div class="post">
            <h4>Name: {{post.name}}</h4>
            <h6>{{post.content}}</h6>
          </div>
        </section>
      </div>
      
      
    </section>
  </div>
</template>

<script>

export default {
  name: 'Forum',
  data: () => ({
    posts: []
  }),
  components: {
    PostForm
  },
  props: {
    artist_id: Number
  },
  mounted() {
    this.getPosts()
  },
  methods: {
    async getPosts() {
      
    }
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