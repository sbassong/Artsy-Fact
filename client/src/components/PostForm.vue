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

export default {
  name: 'Home',
  components: {
  },
  data: () => ({
    reviewer: '',
    content: '',

  }),
  methods: {
    handleChange(event) {
      this[event.target.name] = event.target.value
    },
    handleSubmit(event) {
      event.preventDefault()
      //use the post service to create a record in the posts table here.
    }
  }
}
</script>
