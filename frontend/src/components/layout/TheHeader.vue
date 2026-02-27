<script setup lang="ts">
import { IconSearch, IconSparkles } from '../icons'
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
        <span class="header__breadcrumb-link">{{ breadcrumb[0] }}</span>
        <span class="header__breadcrumb-current">/ {{ breadcrumb[1] }}</span>
      </nav>
    </div>

    <div class="header__right">
      <!-- Search Bar -->
      <div class="header__search">
        <div class="header__search-content">
          <IconSearch :size="20" class="header__search-icon" />
          <span class="header__search-text">Search for anything</span>
        </div>
        <kbd class="header__search-shortcut">⌘K</kbd>
      </div>

      <!-- Book a Call Button -->
      <button class="header__btn">
        Book a Call
      </button>

      <!-- Ask AI Button -->
      <button v-if="!appStore.isAiPanelOpen" class="header__ai-btn" @click="appStore.openAiPanel">
        <IconSparkles :size="20" />
        <span>Ask AI</span>
      </button>
    </div>
  </header>
</template>

<style scoped>
.header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 80px;
  padding: 0 24px;
  background: var(--surface-topbar-bg);
  border-bottom: 1px solid #f0f0f0;
  box-sizing: border-box;
}

.header__left {
  display: flex;
  align-items: center;
  height: 100%;
}

.header__breadcrumb {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 18px;
  line-height: 1;
}

.header__breadcrumb-link {
  color: #9291a5;
  font-weight: 400;
}

.header__breadcrumb-current {
  color: var(--text-primary);
  font-weight: 600;
}

.header__right {
  display: flex;
  align-items: center;
  gap: 12px;
  height: 100%;
}

.header__search {
  display: flex;
  align-items: center;
  justify-content: space-between;
  background: var(--surface-input-bg);
  border: 1px solid var(--outline-sidebar-item);
  border-radius: 12px;
  padding: 0 18px;
  height: 44px;
  width: 340px;
  cursor: pointer;
  box-sizing: border-box;
}

.header__search:hover {
  border-color: var(--color-neutral-300);
}

.header__search-content {
  display: flex;
  align-items: center;
  gap: 8px;
}

.header__search-icon {
  color: var(--text-primary);
  flex-shrink: 0;
}

.header__search-text {
  font-size: 16px;
  font-weight: 500;
  color: var(--text-primary);
}

.header__search-shortcut {
  background: var(--outline-sidebar-item);
  border-radius: 8px;
  padding: 6px 8px;
  font-size: 12px;
  font-weight: 500;
  color: var(--text-primary);
  font-family: inherit;
  border: none;
}

.header__btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: var(--surface-button-secondary-bg);
  border: 1px solid var(--outline-button-neutral);
  border-radius: 12px;
  padding: 0 12px;
  height: 44px;
  font-size: 16px;
  font-weight: 500;
  color: var(--text-primary);
  cursor: pointer;
  font-family: inherit;
  box-sizing: border-box;
}

.header__btn:hover {
  background: var(--color-neutral-50);
}

.header__ai-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  background: var(--surface-button-secondary-bg);
  border: 1px solid var(--outline-button-neutral);
  border-radius: 12px;
  padding: 0 12px;
  height: 44px;
  font-size: 16px;
  font-weight: 500;
  color: var(--text-primary);
  cursor: pointer;
  font-family: inherit;
  box-sizing: border-box;
}

.header__ai-btn:hover {
  background: var(--color-neutral-50);
}

.header__ai-btn svg {
  color: var(--color-primary-600);
}
</style>
