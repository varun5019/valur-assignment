<script setup lang="ts">
interface Props {
  padding?: 'none' | 'sm' | 'md' | 'lg'
}

withDefaults(defineProps<Props>(), {
  padding: 'md'
})
</script>

<template>
  <div :class="['card', `card--padding-${padding}`]">
    <slot />
  </div>
</template>

<style scoped>
.card {
  background: var(--surface-card-bg);
  border-radius: 12px;
  border: 1px solid var(--outline-button-neutral);
}

.card--padding-none {
  padding: 0;
}

.card--padding-sm {
  padding: 1rem;
}

.card--padding-md {
  padding: 1.5rem;
}

.card--padding-lg {
  padding: 2rem;
}
</style>
