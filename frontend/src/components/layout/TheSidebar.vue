<script setup lang="ts">
import { ref } from 'vue'
import BaseIcon from '../ui/BaseIcon.vue'
import BaseButton from '../ui/BaseButton.vue'

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
</script>

<template>
  <aside class="sidebar">
    <!-- Logo -->
    <div class="sidebar__logo">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
        <path d="M12 2L2 22h20L12 2z" fill="#7C3AED" />
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
      <button class="sidebar__promo-close" @click="showPromo = false">
        <BaseIcon name="close" :size="16" />
      </button>
      <h4 class="sidebar__promo-title">Reserve your 2026 energy projects</h4>
      <p class="sidebar__promo-text">
        By submitting, you'll claim your spot in the queue, and we'll be in touch shortly to discuss next steps.
      </p>
      <BaseButton variant="primary" size="md" class="sidebar__promo-btn">
        Claim Your Spot
      </BaseButton>
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
        <BaseIcon name="chevron-up" :size="16" />
      </button>
    </div>
  </aside>
</template>

<style scoped>
.sidebar {
  width: 260px;
  min-width: 260px;
  height: 100vh;
  background: white;
  border-right: 1px solid #E5E7EB;
  display: flex;
  flex-direction: column;
  padding: 1.25rem 0.75rem;
  overflow-y: auto;
}

.sidebar__logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0 0.75rem;
  margin-bottom: 1.5rem;
}

.sidebar__logo-text {
  font-size: 1.25rem;
  font-weight: 700;
  color: #111827;
  letter-spacing: -0.025em;
}

.sidebar__nav {
  flex: 0 0 auto;
}

.sidebar__section {
  margin-bottom: 1.5rem;
}

.sidebar__section-title {
  display: block;
  font-size: 0.6875rem;
  font-weight: 600;
  color: #9CA3AF;
  letter-spacing: 0.05em;
  padding: 0 0.75rem;
  margin-bottom: 0.5rem;
}

.sidebar__menu {
  list-style: none;
  padding: 0;
  margin: 0;
}

.sidebar__menu-item {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.625rem 0.75rem;
  border-radius: 8px;
  color: #6B7280;
  text-decoration: none;
  font-size: 0.875rem;
  font-weight: 500;
  transition: all 0.15s ease;
  cursor: pointer;
}

.sidebar__menu-item:hover {
  background: #F3F4F6;
  color: #374151;
}

.sidebar__menu-item--active {
  background: #F3F0FF;
  color: #7C3AED;
}

.sidebar__menu-item--active:hover {
  background: #F3F0FF;
  color: #7C3AED;
}

.sidebar__spacer {
  flex: 1;
}

.sidebar__promo {
  position: relative;
  background: #F9FAFB;
  border: 1px solid #E5E7EB;
  border-radius: 12px;
  padding: 1rem;
  margin: 0 0.25rem 1rem;
}

.sidebar__promo-close {
  position: absolute;
  top: 0.75rem;
  right: 0.75rem;
  background: none;
  border: none;
  color: #9CA3AF;
  cursor: pointer;
  padding: 0.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

.sidebar__promo-close:hover {
  color: #6B7280;
}

.sidebar__promo-title {
  font-size: 0.875rem;
  font-weight: 600;
  color: #111827;
  margin: 0 0 0.5rem;
  padding-right: 1.5rem;
}

.sidebar__promo-text {
  font-size: 0.75rem;
  color: #6B7280;
  line-height: 1.5;
  margin: 0 0 1rem;
}

.sidebar__promo-btn {
  width: 100%;
}

.sidebar__menu--bottom {
  margin-bottom: 1rem;
}

.sidebar__user {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  border-radius: 8px;
  cursor: pointer;
  transition: background 0.15s ease;
}

.sidebar__user:hover {
  background: #F3F4F6;
}

.sidebar__user-avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #7C3AED;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.75rem;
  font-weight: 600;
}

.sidebar__user-info {
  flex: 1;
  min-width: 0;
}

.sidebar__user-name {
  display: block;
  font-size: 0.875rem;
  font-weight: 500;
  color: #111827;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sidebar__user-email {
  display: block;
  font-size: 0.75rem;
  color: #6B7280;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.sidebar__user-toggle {
  background: none;
  border: none;
  color: #9CA3AF;
  cursor: pointer;
  padding: 0.25rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
