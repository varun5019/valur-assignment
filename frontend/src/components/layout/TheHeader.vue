<script setup lang="ts">
import BaseIcon from '../ui/BaseIcon.vue'
import BaseButton from '../ui/BaseButton.vue'
import { useAppStore } from '../../stores/app'

const appStore = useAppStore()

interface Props {
  breadcrumb?: string[]
}

withDefaults(defineProps<Props>(), {
  breadcrumb: () => ['Dashboard', 'Home']
})
</script>

<template>
  <header class="header">
    <div class="header__left">
      <nav class="header__breadcrumb">
        <template v-for="(item, index) in breadcrumb" :key="index">
          <span :class="{ 'header__breadcrumb-current': index === breadcrumb.length - 1 }">
            {{ item }}
          </span>
          <span v-if="index < breadcrumb.length - 1" class="header__breadcrumb-separator">/</span>
        </template>
      </nav>
    </div>

    <div class="header__right">
      <!-- Search Bar -->
      <div class="header__search">
        <BaseIcon name="search" :size="18" class="header__search-icon" />
        <span class="header__search-text">Search</span>
        <kbd class="header__search-shortcut">⌘K</kbd>
      </div>

      <!-- Book a Call Button -->
      <BaseButton variant="outline" size="md">
        Book a Call
      </BaseButton>

      <!-- Icon Buttons -->
      <button class="header__icon-btn">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7" />
        </svg>
      </button>
      <button class="header__icon-btn">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <circle cx="12" cy="12" r="10" />
          <polyline points="12 6 12 12 16 14" />
        </svg>
      </button>

      <!-- Ask AI Button -->
      <BaseButton variant="secondary" size="md" class="header__ai-btn" @click="appStore.openAiPanel">
        <BaseIcon name="sparkles" :size="16" />
        Ask AI
      </BaseButton>
    </div>
  </header>
</template>

<style scoped>
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 2rem;
  background: white;
  border-bottom: 1px solid #E5E7EB;
}

.header__left {
  display: flex;
  align-items: center;
}

.header__breadcrumb {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  color: #6B7280;
}

.header__breadcrumb-separator {
  color: #D1D5DB;
}

.header__breadcrumb-current {
  color: #111827;
  font-weight: 600;
}

.header__right {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.header__search {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: #F9FAFB;
  border: 1px solid #E5E7EB;
  border-radius: 8px;
  padding: 0.5rem 0.75rem;
  min-width: 180px;
  cursor: pointer;
}

.header__search:hover {
  border-color: #D1D5DB;
}

.header__search-icon {
  color: #9CA3AF;
  flex-shrink: 0;
}

.header__search-text {
  flex: 1;
  font-size: 0.875rem;
  color: #9CA3AF;
}

.header__search-shortcut {
  background: white;
  border: 1px solid #E5E7EB;
  border-radius: 4px;
  padding: 0.125rem 0.375rem;
  font-size: 0.75rem;
  color: #6B7280;
  font-family: inherit;
}

.header__icon-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  color: #9CA3AF;
  padding: 0.5rem;
  border-radius: 6px;
  cursor: pointer;
}

.header__icon-btn:hover {
  background: #F3F4F6;
  color: #6B7280;
}

.header__ai-btn {
  background: #F3F4F6;
}

.header__ai-btn:deep(svg) {
  color: #7C3AED;
}
</style>
