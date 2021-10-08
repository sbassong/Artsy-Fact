<template>
  <div>
      <form @submit='handleSubmit'>
        <label for="name">Name</label>
        <input type="text" placeholder="Enter name here. i.e John " name='name' :value='name' @input='handleChange'>
        <label for="email">Email</label>
        <input type="text" placeholder="Enter Email here. i.e john@email.com" name='email' :value='email' @input='handleChange'>
        <label for="password">Password</label>
        <input type="text" placeholder="Enter password here" name='password' :value='password' @input='handleChange'>
        <button>Register</button>
      </form>

  </div>
</template>

<script>
import {RegisterUser} from '../services/auth'

export default {
  name: 'RegisterForm',
  data: () => ({
    name: '',
    email: '',
    password: ''
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
      const userBody = {
        name: this.name,
        email: this.email,
        password: this.password
      }
      await RegisterUser(userBody)
      this.name = ''
      this.email = ''
      this.password = '' 
      this.$router.push('/users/login')
      }
  }
}
</script>
