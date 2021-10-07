<template>
  <div>

      <form @submit='handleSubmit'>
        <input type="text" name='name' :value='reviewer' @input='handleChange'>
        <input type="text" name='content' :value='content' @input='handleChange'>
        <button>Post</button>
      </form>
      
  </div>
</template>

<script>
import {CreatePost} from '../services/posts'
export default {
  name: 'PostForm',
  data: () => ({
    reviewer: '',
    content: '',

  }),
  props: {
    artist_id: Number
  },
  methods: {
    handleChange(event) {
      this[event.target.name] = event.target.value
    },
    async handleSubmit(event) {
      event.preventDefault()
      //use the post service to create a record in the posts table here.
      const postBody = {
        name: this.reviewer,
        content: this.content,
        artist_id: this.artist_id
      }

      await CreatePost(postBody)
    }
  }
}
</script>
