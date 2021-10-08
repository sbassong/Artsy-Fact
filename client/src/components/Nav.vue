<template>
  <div class="nav justify-content-space-between">

    <ul class="nav justify-content-start">
      <li class="nav-item">
        <a class="nav-link active" aria-current="page" href="/">Artsy_Facts</a>
      </li>
    </ul>
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
        <a class="nav-link" href="/users/register">Sign Up</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="/users/login">Sign In</a>
      </li>
    </ul>
  </div>

</template>

<script>

export default {
  name: 'Nav',
  data:()=> ({
    clickedRegister: false,
    clickedLogin: false
  }),
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
