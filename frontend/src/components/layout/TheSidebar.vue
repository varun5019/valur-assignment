<script setup lang="ts">
import { ref } from 'vue'
import BaseIcon from '../ui/BaseIcon.vue'

interface NavItem {
  id: string
  label: string
  icon: string
  route?: string
}

const activeItem = ref('dashboard')
const showPromo = ref(true)

const coreWorkflowItems: NavItem[] = [
  { id: 'dashboard', label: 'Dashboard', icon: 'dashboard', route: '/' },
  { id: 'documents', label: 'Documents', icon: 'documents', route: '/documents' },
  { id: 'solar-activities', label: 'Solar Activities', icon: 'solar', route: '/solar-activities' },
]

const planningItems: NavItem[] = [
  { id: 'guided-planning', label: 'Guided Planning', icon: 'planning', route: '/guided-planning' },
  { id: 'solar-projects', label: 'Solar Projects', icon: 'projects', route: '/solar-projects' },
  { id: 'tax-calculators', label: 'Tax Saving Calculators', icon: 'calculator', route: '/tax-calculators' },
]

const bottomItems: NavItem[] = [
  { id: 'settings', label: 'Settings', icon: 'settings', route: '/settings' },
  { id: 'support', label: 'Support', icon: 'support', route: '/support' },
]

function setActive(id: string) {
  activeItem.value = id
}

function closePromo() {
  showPromo.value = false
}
</script>

<template>
  <aside class="sidebar">
    <!-- Logo -->
    <div class="sidebar__logo">
      <svg width="24" height="25" viewBox="0 0 24 25" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 0L24 25H0L12 0Z" fill="#3D5BD9"/>
      </svg>
      <span class="sidebar__logo-text">VALUR</span>
    </div>

    <!-- Navigation -->
    <nav class="sidebar__nav">
      <!-- Core Workflow Section -->
      <div class="sidebar__section">
        <span class="sidebar__section-title">CORE WORKFLOW</span>
        <ul class="sidebar__menu">
          <li v-for="item in coreWorkflowItems" :key="item.id">
            <router-link
              :to="item.route || '/'"
              :class="['sidebar__menu-item', { 'sidebar__menu-item--active': activeItem === item.id }]"
              @click="setActive(item.id)"
            >
              <BaseIcon :name="item.icon" :size="20" />
              <span>{{ item.label }}</span>
            </router-link>
          </li>
        </ul>
      </div>

      <!-- Planning & Strategy Section -->
      <div class="sidebar__section">
        <span class="sidebar__section-title">PLANNING & STRATEGY</span>
        <ul class="sidebar__menu">
          <li v-for="item in planningItems" :key="item.id">
            <router-link
              :to="item.route || '/'"
              :class="['sidebar__menu-item', { 'sidebar__menu-item--active': activeItem === item.id }]"
              @click="setActive(item.id)"
            >
              <BaseIcon :name="item.icon" :size="20" />
              <span>{{ item.label }}</span>
            </router-link>
          </li>
        </ul>
      </div>
    </nav>

    <!-- Spacer -->
    <div class="sidebar__spacer"></div>

    <!-- Promo Card -->
    <div v-if="showPromo" class="sidebar__promo">
      <button class="sidebar__promo-close" @click="closePromo" aria-label="Close">
        <BaseIcon name="close" :size="12" />
      </button>
      <h4 class="sidebar__promo-title">Reserve your 2026 energy projects</h4>
      <p class="sidebar__promo-text">
        By submitting, you'll claim your spot in the queue, and we'll be in touch shortly to discuss next steps.
      </p>
      <button class="sidebar__promo-btn">
        Claim Your Spot
      </button>
    </div>

    <!-- Bottom Menu -->
    <ul class="sidebar__menu sidebar__menu--bottom">
      <li v-for="item in bottomItems" :key="item.id">
        <router-link
          :to="item.route || '/'"
          :class="['sidebar__menu-item', { 'sidebar__menu-item--active': activeItem === item.id }]"
          @click="setActive(item.id)"
        >
          <BaseIcon :name="item.icon" :size="20" />
          <span>{{ item.label }}</span>
        </router-link>
      </li>
    </ul>

    <!-- User Profile -->
    <div class="sidebar__user">
      <div class="sidebar__user-avatar">
        <span>SM</span>
      </div>
      <div class="sidebar__user-info">
        <span class="sidebar__user-name">Scott McTominay</span>
        <span class="sidebar__user-email">scottmctominay@gmail.com</span>
      </div>
      <button class="sidebar__user-toggle">
        <BaseIcon name="chevron-up" :size="20" />
      </button>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 296px;
  min-width: 296px;
  height: 100vh;
  background: var(--surface-sidebar-bg);
  border-right: 1px solid var(--outline-sidebar-item);
  display: flex;
  flex-direction: column;
  padding: 24px;
  overflow-y: auto;
}

.sidebar__logo {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-bottom: 32px;
}

.sidebar__logo-text {
  font-family: var(--font-family);
  font-size: 20px;
  font-weight: 700;
  color: var(--text-primary);
  letter-spacing: 0.05em;
}

.sidebar__nav {
  flex: 0 0 auto;
  display: flex;
  flex-direction: column;
  gap: 16px;
}

.sidebar__section {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.sidebar__section-title {
  font-family: var(--font-family);
  font-size: 12px;
  font-weight: 500;
  color: var(--icon-sidebar-inactive);
  letter-spacing: 0;
}

.sidebar__menu {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.sidebar__menu-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  border-radius: 8px;
  color: var(--text-primary);
  text-decoration: none;
  font-family: var(--font-family);
  font-size: 16px;
  font-weight: 500;
  background: var(--surface-sidebar-item);
  transition: all 0.15s ease;
  cursor: pointer;
}

.sidebar__menu-item svg {
  color: var(--icon-sidebar-inactive);
  transition: color 0.15s ease;
}

.sidebar__menu-item:hover {
  background: rgba(255, 255, 255, 0.5);
}

.sidebar__menu-item:hover svg {
  color: var(--icon-sidebar-active);
}

.sidebar__menu-item--active {
  background: var(--surface-sidebar-item-active);
  border: 1px solid var(--outline-sidebar-item);
  color: var(--text-primary);
}

.sidebar__menu-item--active svg {
  color: var(--icon-sidebar-active);
}

.sidebar__menu-item--active:hover {
  background: var(--surface-sidebar-item-active);
}

.sidebar__spacer {
  flex: 1;
}

.sidebar__promo {
  position: relative;
  background: var(--surface-sidebar-card);
  border: 1px solid var(--outline-sidebar-item);
  border-radius: 12px;
  padding: 12px;
  margin-bottom: 4px;
}

.sidebar__promo-close {
  position: absolute;
  top: 8px;
  right: 8px;
  background: none;
  border: none;
  color: var(--text-secondary);
  cursor: pointer;
  padding: 4px;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 0;
}

.sidebar__promo-close:hover {
  color: var(--color-neutral-700);
}

.sidebar__promo-title {
  font-family: var(--font-family);
  font-size: 14px;
  font-weight: 500;
  color: var(--text-primary);
  margin: 0 0 4px;
  padding-right: 20px;
  line-height: 1.4;
}

.sidebar__promo-text {
  font-family: var(--font-family);
  font-size: 12px;
  font-weight: 400;
  color: var(--text-secondary);
  line-height: 1.4;
  margin: 0 0 12px;
}

.sidebar__promo-btn {
  width: 100%;
  background: linear-gradient(90deg, #785fe0 0%, #3d6ed8 100%);
  border: none;
  border-radius: 8px;
  padding: 6px 8px;
  font-family: var(--font-family);
  font-size: 12px;
  font-weight: 600;
  color: var(--text-inverted);
  cursor: pointer;
  transition: opacity 0.15s ease;
}

.sidebar__promo-btn:hover {
  opacity: 0.9;
}

.sidebar__menu--bottom {
  margin-bottom: 4px;
}

.sidebar__user {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 12px;
  background: var(--surface-sidebar-card);
  border: 1px solid var(--outline-sidebar-item);
  border-radius: 12px;
  cursor: pointer;
  transition: background 0.15s ease;
}

.sidebar__user:hover {
  background: var(--color-neutral-50);
}

.sidebar__user-avatar {
  width: 28px;
  height: 28px;
  border-radius: 50%;
  background: linear-gradient(90deg, #785fe0 0%, #3d6ed8 100%);
  color: var(--text-inverted);
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: var(--font-family);
  font-size: 12px;
  font-weight: 500;
  flex-shrink: 0;
}

.sidebar__user-info {
  flex: 1;
  min-width: 0;
  display: flex;
  flex-direction: column;
}

.sidebar__user-name {
  font-family: var(--font-family);
  font-size: 16px;
  font-weight: 500;
  color: var(--text-primary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1.2;
}

.sidebar__user-email {
  font-family: var(--font-family);
  font-size: 12px;
  font-weight: 400;
  color: var(--text-secondary);
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  line-height: 1.2;
}

.sidebar__user-toggle {
  background: none;
  border: none;
  color: var(--text-primary);
  cursor: pointer;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}
</style>
