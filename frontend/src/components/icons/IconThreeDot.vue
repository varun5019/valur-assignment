<script setup lang="ts">
defineProps<{
  size?: number
}>()
</script>

<template>
  <svg
    :width="size || 20"
    :height="size || 20"
    viewBox="0 0 20 20"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <circle cx="10" cy="4.16667" r="1.25" fill="currentColor" />
    <circle cx="10" cy="10" r="1.25" fill="currentColor" />
    <circle cx="10" cy="15.8333" r="1.25" fill="currentColor" />
  </svg>
</template>
