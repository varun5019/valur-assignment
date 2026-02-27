<script setup lang="ts">
import { IconSparkles, IconArrowDown, IconThreeDot } from '../icons'

interface Strategy {
  id: string
  date: string
  title: string
  amount: string
  change: string
}

const strategies: Strategy[] = [
  {
    id: '1',
    date: '12 Dec 2025',
    title: 'Solar Investment Tax Credits',
    amount: '$11,756',
    change: '12.75%',
  },
  {
    id: '2',
    date: '12 Dec 2025',
    title: 'Solar Investment Tax Credits',
    amount: '$11,756',
    change: '12.75%',
  },
]
</script>

<template>
  <div class="strategies-card">
    <div class="strategies-card__header">
      <div class="strategies-card__header-info">
        <span class="strategies-card__subtitle">Your Strategies</span>
        <h3 class="strategies-card__title">2 Strategies</h3>
      </div>
      <div class="strategies-card__actions">
        <button class="strategies-card__dropdown">
          Last 6 months
          <IconArrowDown :size="16" />
        </button>
        <button class="strategies-card__more">
          <IconThreeDot :size="18" />
        </button>
      </div>
    </div>

    <div class="strategies-card__divider"></div>

    <!-- Card Container -->
    <div class="strategies-card__list">
      <!-- AI Recommendation -->
      <div class="strategies-card__ai-rec">
        <div class="strategies-card__ai-rec-content">
          <div class="strategies-card__ai-rec-icon">
            <IconSparkles :size="20" />
          </div>
          <div class="strategies-card__ai-rec-text">
            <span class="strategies-card__ai-rec-title">AI Recommendation - Charitable Remainder Trust</span>
            <span class="strategies-card__ai-rec-desc">CRUT reduces taxes while supporting your charity.</span>
          </div>
        </div>
        <button class="strategies-card__ai-rec-btn">
          Check Viability
        </button>
      </div>

      <!-- Strategy Items -->
      <div
        v-for="strategy in strategies"
        :key="strategy.id"
        class="strategies-card__item"
      >
        <div class="strategies-card__item-info">
          <span class="strategies-card__item-date">{{ strategy.date }}</span>
          <span class="strategies-card__item-title">{{ strategy.title }}</span>
        </div>
        <div class="strategies-card__item-value">
          <span class="strategies-card__item-amount">{{ strategy.amount }}</span>
          <span class="strategies-card__item-change">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M6 2L10 6H7V10H5V6H2L6 2Z" fill="#22C55E"/>
            </svg>
            {{ strategy.change }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.strategies-card {
  background: var(--surface-card-bg);
  border-radius: 20px;
  border: 1px solid var(--outline-button-neutral);
  padding: 24px;
  height: 100%;
  display: flex;
  flex-direction: column;
  gap: 24px;
}

.strategies-card__header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.strategies-card__header-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.strategies-card__subtitle {
  font-size: 18px;
  font-weight: 400;
  color: var(--text-secondary);
}

.strategies-card__title {
  font-size: 22px;
  font-weight: 600;
  color: var(--text-primary);
  margin: 0;
}

.strategies-card__actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.strategies-card__dropdown {
  display: flex;
  align-items: center;
  gap: 4px;
  background: var(--surface-button-secondary-bg);
  border: 1px solid var(--outline-button-neutral);
  border-radius: 8px;
  padding: 8px;
  font-size: 12px;
  font-weight: 500;
  color: var(--text-primary);
  cursor: pointer;
  font-family: inherit;
}

.strategies-card__dropdown:hover {
  background: var(--color-neutral-50);
}

.strategies-card__more {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--surface-button-secondary-bg);
  border: 1px solid var(--outline-button-neutral);
  border-radius: 8px;
  padding: 8px;
  color: var(--text-primary);
  cursor: pointer;
}

.strategies-card__more:hover {
  background: var(--color-neutral-50);
}

.strategies-card__divider {
  height: 1px;
  background: var(--outline-button-neutral);
  width: 100%;
}

.strategies-card__ai-rec {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 12px;
  background: linear-gradient(95.38deg, rgb(252, 238, 253) 1.86%, rgb(216, 223, 251) 100.47%);
  border-radius: 12px;
  padding: 12px;
}

.strategies-card__ai-rec-content {
  display: flex;
  align-items: flex-start;
  gap: 4px;
}

.strategies-card__ai-rec-icon {
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  color: var(--color-primary-600);
}

.strategies-card__ai-rec-text {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.strategies-card__ai-rec-title {
  font-size: 14px;
  font-weight: 700;
  color: var(--text-primary);
}

.strategies-card__ai-rec-desc {
  font-size: 12px;
  font-weight: 400;
  line-height: 16px;
  color: var(--text-secondary);
}

.strategies-card__ai-rec-btn {
  flex-shrink: 0;
  background: var(--surface-button-primary-bg);
  border: 1px solid var(--outline-button-focus);
  border-radius: 8px;
  padding: 8px;
  font-size: 12px;
  font-weight: 500;
  color: var(--text-inverted);
  cursor: pointer;
  font-family: inherit;
}

.strategies-card__ai-rec-btn:hover {
  opacity: 0.9;
}

.strategies-card__list {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.strategies-card__item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 12px;
  background: var(--surface-card-item-bg);
  border-radius: 12px;
}

.strategies-card__item-info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.strategies-card__item-date {
  font-size: 14px;
  font-weight: 400;
  color: var(--text-secondary);
}

.strategies-card__item-title {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-primary);
}

.strategies-card__item-value {
  display: flex;
  align-items: flex-end;
  gap: 4px;
}

.strategies-card__item-amount {
  font-size: 22px;
  font-weight: 700;
  color: var(--text-primary);
}

.strategies-card__item-change {
  display: flex;
  align-items: center;
  gap: 4px;
  font-size: 14px;
  font-weight: 400;
  color: var(--text-success);
  padding: 1px 0;
}
</style>
