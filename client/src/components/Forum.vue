<template>
  <div class="forum">

    <section class="post-form-cont">
      <div>
        <button class='show-form-button' @click='renderForm'>Add Review</button>
        <PostForm :user_id="user_id" :artist_id='artist_id' v-if='clicked'/>
      </div>
    </section>

    <section class="posts">
        <h3>Posts</h3>
      <div>
        <section v-for='post in posts' :key='post.id'>
          <div class="post">
            <h4>Reviewer: {{post.reviewer}}</h4>
            <h5>{{post.content}}</h5>
            <!-- <div v-if='user && authenticated' > -->
              <button @click='deletePost(post.id)' >Delete Post</button>
            <!-- </div> -->
          </div>
        </section>
      </div>
    </section>

  </div>
</template>

<script>
import PostForm from './PostForm.vue'
import {RemovePost} from '../services/posts'

export default {
  name: 'Forum',
  data: () => ({
    clicked: false
  }),
  components: {
    PostForm,
  },
  props: {
    posts: Array,
    artist_id: Number
  },
  methods: {
    renderForm() {
      this.clicked ? this.clicked=false : this.clicked=true
    },
    async deletePost(post_id) {
      await RemovePost(post_id)
    }
  }
}
</script>

<style scoped>
  .post {
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