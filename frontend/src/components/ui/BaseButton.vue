<script setup lang="ts">
interface Props {
  variant?: 'primary' | 'secondary' | 'ghost' | 'outline'
  size?: 'sm' | 'md' | 'lg'
}

withDefaults(defineProps<Props>(), {
  variant: 'primary',
  size: 'md'
})
</script>

<template>
  <button :class="['btn', `btn--${variant}`, `btn--${size}`]">
    <slot />
  </button>
</template>

<style scoped>
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 0.5rem;
  font-weight: 500;
  border-radius: 8px;
  border: none;
  cursor: pointer;
  transition: all 0.2s ease;
  font-family: inherit;
}

.btn--sm {
  padding: 0.375rem 0.75rem;
  font-size: 0.8125rem;
}

.btn--md {
  padding: 0.5rem 1rem;
  font-size: 0.875rem;
}

.btn--lg {
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
}

.btn--primary {
  background: #7C3AED;
  color: white;
}

.btn--primary:hover {
  background: #6D28D9;
}

.btn--secondary {
  background: #F3F4F6;
  color: #374151;
}

.btn--secondary:hover {
  background: #E5E7EB;
}

.btn--ghost {
  background: transparent;
  color: #374151;
}

.btn--ghost:hover {
  background: #F3F4F6;
}

.btn--outline {
  background: white;
  color: #374151;
  border: 1px solid #E5E7EB;
}

.btn--outline:hover {
  background: #F9FAFB;
  border-color: #D1D5DB;
}
</style>
