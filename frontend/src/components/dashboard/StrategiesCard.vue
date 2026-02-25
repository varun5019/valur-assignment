<script setup lang="ts">
import BaseIcon from '../ui/BaseIcon.vue'
import BaseButton from '../ui/BaseButton.vue'

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
      <h3 class="strategies-card__title">Your Strategies</h3>
      <div class="strategies-card__actions">
        <button class="strategies-card__dropdown">
          Last 6 months
          <BaseIcon name="chevron-down" :size="16" />
        </button>
        <button class="strategies-card__more">
          <BaseIcon name="more" :size="18" />
        </button>
      </div>
    </div>

    <div class="strategies-card__count">2 Strategies</div>

    <!-- AI Recommendation -->
    <div class="strategies-card__ai-rec">
      <div class="strategies-card__ai-rec-content">
        <div class="strategies-card__ai-rec-icon">
          <BaseIcon name="sparkles" :size="16" />
        </div>
        <div class="strategies-card__ai-rec-text">
          <span class="strategies-card__ai-rec-title">AI Recommendation - Charitable Remainder Trust</span>
          <span class="strategies-card__ai-rec-desc">CRUT reduces taxes while supporting your charity.</span>
        </div>
      </div>
      <BaseButton variant="outline" size="sm" class="strategies-card__ai-rec-btn">
        Check Viability
      </BaseButton>
    </div>

    <!-- Strategy List -->
    <div class="strategies-card__list">
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
            <BaseIcon name="trending-up" :size="12" />
            {{ strategy.change }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.strategies-card {
  background: white;
  border-radius: 12px;
  border: 1px solid #E5E7EB;
  padding: 1.5rem;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.strategies-card__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.25rem;
}

.strategies-card__title {
  font-size: 0.9375rem;
  font-weight: 500;
  color: #6B7280;
  margin: 0;
}

.strategies-card__actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.strategies-card__dropdown {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  background: none;
  border: 1px solid #E5E7EB;
  border-radius: 6px;
  padding: 0.375rem 0.75rem;
  font-size: 0.8125rem;
  color: #374151;
  cursor: pointer;
  font-family: inherit;
}

.strategies-card__dropdown:hover {
  background: #F9FAFB;
}

.strategies-card__more {
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  color: #9CA3AF;
  cursor: pointer;
  padding: 0.25rem;
}

.strategies-card__more:hover {
  color: #6B7280;
}

.strategies-card__count {
  font-size: 1.5rem;
  font-weight: 700;
  color: #111827;
  margin-bottom: 1.25rem;
}

.strategies-card__ai-rec {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1rem;
  background: linear-gradient(135deg, #FEFCE8 0%, #FEF3C7 50%, #FDE68A 100%);
  border: 1px solid #FDE68A;
  border-radius: 10px;
  padding: 1rem;
  margin-bottom: 1rem;
}

.strategies-card__ai-rec-content {
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  flex: 1;
  min-width: 0;
}

.strategies-card__ai-rec-icon {
  width: 28px;
  height: 28px;
  background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.strategies-card__ai-rec-text {
  display: flex;
  flex-direction: column;
  gap: 0.125rem;
  min-width: 0;
}

.strategies-card__ai-rec-title {
  font-size: 0.8125rem;
  font-weight: 600;
  color: #111827;
}

.strategies-card__ai-rec-desc {
  font-size: 0.75rem;
  color: #6B7280;
}

.strategies-card__ai-rec-btn {
  flex-shrink: 0;
  background: white;
}

.strategies-card__list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.strategies-card__item {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  background: #F9FAFB;
  border-radius: 10px;
  gap: 1rem;
}

.strategies-card__item-info {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  min-width: 0;
}

.strategies-card__item-date {
  font-size: 0.75rem;
  color: #9CA3AF;
}

.strategies-card__item-title {
  font-size: 0.875rem;
  font-weight: 600;
  color: #111827;
}

.strategies-card__item-value {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.25rem;
}

.strategies-card__item-amount {
  font-size: 1.125rem;
  font-weight: 700;
  color: #111827;
}

.strategies-card__item-change {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.75rem;
  font-weight: 500;
  color: #10B981;
}
</style>
