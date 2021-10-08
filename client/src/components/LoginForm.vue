<template>
  <div>
      <form @submit='handleSubmit'>
        <label for="email">Email</label>
        <input type="text" placeholder="john@email.com" name='email' :value='email' @input='handleChange'>
        <label for="password">Password</label>
        <input type="text" placeholder="Enter password here" name='password' :value='password' @input='handleChange'>
        <button>Log In</button>
      </form>

  </div>
</template>

<script>
import {LoginUser} from '../services/auth'

export default {
  name: 'LoginForm',
  data: () => ({
    email: '',
    password: ''
  }),
  methods: {
    handleChange(event) {
      this[event.target.name] = event.target.value
    },
    async handleSubmit(event) {
      event.preventDefault()
      const loginBody = {
        email: this.email,
        password: this.password
      }
      await LoginUser(loginBody)
      this.email = ''
      this.password = ''
      this.$router.push('/')
    }
  }
}
</script>
