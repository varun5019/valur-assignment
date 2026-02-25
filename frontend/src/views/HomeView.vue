<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { api } from '../services/api'
import { useAppStore } from '../stores/app'

const appStore = useAppStore()
const message = ref<string>('Checking API connection...')

onMounted(async () => {
  appStore.setLoading(true)
  try {
    const response = await api.healthCheck()
    message.value = response.data.message
    appStore.setApiStatus('healthy')
  } catch (error) {
    message.value = 'Failed to connect to API'
    appStore.setApiStatus('error')
  } finally {
    appStore.setLoading(false)
  }
})
</script>

<template>
  <main>
    <h1>Welcome to Vue + Django</h1>
    <div class="status-card">
      <h2>API Status</h2>
      <p :class="['status', appStore.apiStatus]">{{ message }}</p>
    </div>
    <div class="links">
      <router-link to="/about">About</router-link>
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
  margin-bottom: 2rem;
}

.status-card {
  background: #f5f5f5;
  border-radius: 8px;
  padding: 1.5rem;
  max-width: 400px;
  margin: 0 auto 2rem;
}

.status {
  font-weight: bold;
  padding: 0.5rem;
  border-radius: 4px;
}

.status.healthy {
  color: #2e7d32;
  background: #e8f5e9;
}

.status.error {
  color: #c62828;
  background: #ffebee;
}

.status.unknown {
  color: #f57c00;
  background: #fff3e0;
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
