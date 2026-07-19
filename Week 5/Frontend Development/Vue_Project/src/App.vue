<template>
  <div>
    <h1>Student Portal</h1>

    <nav>
      <RouterLink to="/">Courses</RouterLink> |
      <RouterLink to="/profile">Profile</RouterLink>
    </nav>

    <hr>

    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<style>
body {
  font-family: Arial, sans-serif;
  margin: 20px;
}

nav {
  margin: 15px 0;
}

a {
  margin-right: 10px;
}
</style>