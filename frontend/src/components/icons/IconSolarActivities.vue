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
    <circle cx="10" cy="10" r="4.16667" stroke="currentColor" stroke-width="1.5" />
    <path d="M10 1.66667V3.33333" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
    <path d="M10 16.6667V18.3333" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
    <path d="M18.3333 10H16.6667" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
    <path d="M3.33333 10H1.66667" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
    <path d="M15.8926 4.10744L14.7141 5.28592" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
    <path d="M5.28595 14.714L4.10747 15.8925" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
    <path d="M15.8926 15.8926L14.7141 14.7141" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
    <path d="M5.28595 5.28601L4.10747 4.10754" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
  </svg>
</template>
