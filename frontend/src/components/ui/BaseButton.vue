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
  font-family: var(--font-family);
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
  background: var(--surface-button-primary-bg);
  color: var(--text-inverted);
}

.btn--primary:hover {
  background: var(--color-primary-600);
}

.btn--primary:focus {
  outline: 2px solid var(--outline-button-focus);
  outline-offset: 2px;
}

.btn--secondary {
  background: var(--surface-card-item-bg);
  color: var(--color-neutral-700);
}

.btn--secondary:hover {
  background: var(--color-neutral-200);
}

.btn--ghost {
  background: transparent;
  color: var(--color-neutral-700);
}

.btn--ghost:hover {
  background: var(--surface-card-item-bg);
}

.btn--outline {
  background: var(--surface-button-secondary-bg);
  color: var(--color-neutral-700);
  border: 1px solid var(--outline-button-neutral);
}

.btn--outline:hover {
  background: var(--color-neutral-50);
  border-color: var(--color-neutral-300);
}

.btn--outline:focus {
  outline: 2px solid var(--outline-button-focus);
  outline-offset: 2px;
}
</style>
