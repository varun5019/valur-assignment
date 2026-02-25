<script setup lang="ts">
</script>

<template>
  <main>
    <h1>About</h1>
    <p>This is a Vue.js + Django full-stack project template.</p>
    <div class="features">
      <h2>Features</h2>
      <ul>
        <li><strong>Frontend:</strong> Vue 3, TypeScript, Vite, Vue Router, Pinia</li>
        <li><strong>Backend:</strong> Django, Django REST Framework, SQLite</li>
        <li><strong>API:</strong> Axios for HTTP requests</li>
        <li><strong>CORS:</strong> Configured for development</li>
      </ul>
    </div>
    <div class="links">
      <router-link to="/">Back to Home</router-link>
    </div>
  </main>
</template>

<style scoped>
main {
  text-align: center;
  padding: 2rem;
}

h1 {
  color: #42b883;
  margin-bottom: 1rem;
}

.features {
  text-align: left;
  max-width: 500px;
  margin: 2rem auto;
  padding: 1.5rem;
  background: #f5f5f5;
  border-radius: 8px;
}

.features h2 {
  margin-bottom: 1rem;
  color: #333;
}

.features ul {
  list-style: disc;
  padding-left: 1.5rem;
}

.features li {
  margin-bottom: 0.5rem;
}

.links {
  margin-top: 1rem;
}

.links a {
  color: #42b883;
  text-decoration: none;
  font-weight: 500;
}

.links a:hover {
  text-decoration: underline;
}
</style>
