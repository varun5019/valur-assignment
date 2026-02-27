<script setup lang="ts">
defineProps<{
  size?: number
}>()
</script>

<template>
  <svg 
    :width="size || 14" 
    :height="size || 14" 
    viewBox="0 0 14 14" 
    fill="none" 
    xmlns="http://www.w3.org/2000/svg"
  >
    <path 
      d="M7 9.33V7m0-2.33h.007M12.833 7A5.833 5.833 0 1 1 1.167 7a5.833 5.833 0 0 1 11.666 0Z" 
      stroke="currentColor" 
      stroke-width="1.17" 
      stroke-linecap="round" 
      stroke-linejoin="round"
    />
  </svg>
</template>
