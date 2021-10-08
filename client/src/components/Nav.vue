<template>

<ul class="nav justify-content-end">
  <li class="nav-item">
    <a class="nav-link active" aria-current="page" href="/">Home</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/artists">Artists</a>
  </li>
  <li class="nav-item">
    <a class="nav-link" href="/about">About</a>
  </li>
  <li class="nav-item">
    <!-- <a class="nav-link" href="/about"> -->
      <button @click='renderRegisterForm'>Sign Up</button>
      <div v-if='clickedRegister'>
        <RegisterForm />
      </div>
    <!-- </a> -->
  </li>
  <li class="nav-item">
    <!-- <a class="nav-link" href="/about"> -->
      <button @click='renderLoginForm'>Sign in</button>
      <div v-if="clickedLogin">
        <LoginForm />
      </div>
    <!-- </a> -->
  </li>
  
</ul>

</template>

<script>
import RegisterForm from '../components/RegisterForm.vue'
import LoginForm from '../components/LoginForm.vue'

export default {
  name: 'Nav',
  data:()=> ({
    clickedRegister: false,
    clickedLogin: false
  }),
  components:{
    RegisterForm,
    LoginForm
  },
  methods: {
    renderLoginForm() {
      this.clickedLogin ? this.clickedLogin=false : this.clickedLogin=true
    },
    renderRegisterForm() {
      this.clickedRegister ? this.clickedRegister=false : this.clickedRegister=true
    }
  }
}
</script>
