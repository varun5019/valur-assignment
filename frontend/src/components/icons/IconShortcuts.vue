<script setup lang="ts">
withDefaults(defineProps<{ size?: number }>(), { size: 24 })
</script>

<template>
  <svg :width="size" :height="size" viewBox="0 0 24 24" fill="none">
    <rect x="3" y="3" width="18" height="18" rx="3" stroke="currentColor" stroke-width="1.5"/>
    <line x1="9" y1="3" x2="9" y2="21" stroke="currentColor" stroke-width="1.5"/>
  </svg>
</template>
