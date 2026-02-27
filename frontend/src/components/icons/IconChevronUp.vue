<script setup lang="ts">
withDefaults(defineProps<{ size?: number }>(), { size: 24 })
</script>

<template>
  <svg :width="size" :height="size" viewBox="0 0 24 24" fill="none">
    <path d="M18 15L12 9L6 15" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
  </svg>
</template>
