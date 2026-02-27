<script setup lang="ts">
import TaxSavingsCard from '../components/dashboard/TaxSavingsCard.vue'
import StrategiesCard from '../components/dashboard/StrategiesCard.vue'

const userName = 'Scott'
</script>

<template>
  <div class="dashboard">
    <div class="dashboard__greeting">
      <h1 class="dashboard__title">Hi there, {{ userName }} 👋</h1>
      <p class="dashboard__subtitle">View your investment strategies here...</p>
    </div>

    <div class="dashboard__grid">
      <TaxSavingsCard class="dashboard__card" />
      <StrategiesCard class="dashboard__card" />
    </div>
  </div>
</template>

<style scoped>
.dashboard {
  padding: 2rem;
  background: var(--surface-page-bg);
  min-height: calc(100vh - 65px);
}

.dashboard__greeting {
  margin-bottom: 1.5rem;
}

.dashboard__title {
  font-size: 1.75rem;
  font-weight: 700;
  color: var(--text-primary);
  margin: 0 0 0.25rem;
}

.dashboard__subtitle {
  font-size: 0.9375rem;
  color: var(--text-secondary);
  margin: 0;
}

.dashboard__grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 1.5rem;
}

.dashboard__card {
  min-height: 420px;
}

@media (max-width: 500px) {
  .dashboard__grid {
    grid-template-columns: 1fr;
  }
  
  .dashboard__card {
    min-height: auto;
  }
}
</style>
