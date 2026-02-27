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
      d="M10 1.66667V3.33333M10 16.6667V18.3333M10 6.66667C8.15905 6.66667 6.66667 8.15905 6.66667 10C6.66667 11.841 8.15905 13.3333 10 13.3333C11.841 13.3333 13.3333 11.841 13.3333 10C13.3333 8.15905 11.841 6.66667 10 6.66667ZM10 6.66667V3.33333M3.33333 10H1.66667M18.3333 10H16.6667M4.69669 4.69669L3.51472 3.51472M16.4853 16.4853L15.3033 15.3033M4.69669 15.3033L3.51472 16.4853M16.4853 3.51472L15.3033 4.69669"
      stroke="currentColor"
      stroke-width="1.5"
      stroke-linecap="round"
      stroke-linejoin="round"
    />
  </svg>
</template>
