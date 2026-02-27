<script setup lang="ts">
defineProps<{
  size?: number
}>()
</script>

<template>
  <svg 
    :width="size || 16" 
    :height="size || 16" 
    viewBox="0 0 16 16" 
    fill="none" 
    xmlns="http://www.w3.org/2000/svg"
  >
    <path 
      d="M6.06 6a2 2 0 0 1 3.88.67c0 1.33-2 2-2 2M8 11.33h.01M14.67 8A6.67 6.67 0 1 1 1.33 8a6.67 6.67 0 0 1 13.34 0Z" 
      stroke="currentColor" 
      stroke-width="1.33" 
      stroke-linecap="round" 
      stroke-linejoin="round"
    />
  </svg>
</template>
