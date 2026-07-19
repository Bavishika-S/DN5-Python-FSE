<template>
  <div>
    <h2>Courses</h2>

    <div v-for="course in courses" :key="course.id">
      <h3>{{ course.name }}</h3>
      <p>Credits: {{ course.credits }}</p>
      <hr>
    </div>
  </div>
</template>

<script setup>
const courses = [
  { id: 1, name: 'Web Development', credits: 4 },
  { id: 2, name: 'React', credits: 4 },
  { id: 3, name: 'Angular', credits: 3 },
  { id: 4, name: 'Vue', credits: 3 },
  { id: 5, name: 'Python', credits: 4 }
]
</script>