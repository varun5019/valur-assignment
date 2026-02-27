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
    <path
      d="M11.6667 2.5H17.5V8.33333M8.33333 17.5H2.5V11.6667M17.5 2.5L11.25 8.75M2.5 17.5L8.75 11.25"
      stroke="currentColor"
      stroke-width="1.66667"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
</template>
