<script setup lang="ts">
import { ref, computed, onMounted } from 'vue'
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Filler,
} from 'chart.js'
import BaseIcon from '../ui/BaseIcon.vue'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Filler
)

const selectedMonth = ref('Mar')
const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']

const chartData = computed(() => ({
  labels: months,
  datasets: [
    {
      data: [2000, 3500, 5000, 4200, 4800, 5200, 5500],
      borderColor: '#7C3AED',
      backgroundColor: 'rgba(124, 58, 237, 0.1)',
      fill: true,
      tension: 0.4,
      pointRadius: months.map(m => m === selectedMonth.value ? 6 : 0),
      pointBackgroundColor: '#7C3AED',
      pointBorderColor: 'white',
      pointBorderWidth: 2,
      pointHoverRadius: 6,
    },
  ],
}))

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false,
    },
    tooltip: {
      enabled: true,
      backgroundColor: '#1F2937',
      titleColor: 'white',
      bodyColor: 'white',
      padding: 12,
      cornerRadius: 8,
      displayColors: false,
      callbacks: {
        label: (context: any) => `$${context.raw.toLocaleString()}`,
      },
    },
  },
  scales: {
    x: {
      grid: {
        display: false,
      },
      border: {
        display: false,
      },
      ticks: {
        color: '#9CA3AF',
        font: {
          size: 12,
        },
      },
    },
    y: {
      display: false,
      grid: {
        display: false,
      },
    },
  },
  interaction: {
    intersect: false,
    mode: 'index' as const,
  },
}
</script>

<template>
  <div class="tax-savings-card">
    <div class="tax-savings-card__header">
      <h3 class="tax-savings-card__title">Tax Savings</h3>
      <div class="tax-savings-card__actions">
        <button class="tax-savings-card__dropdown">
          Last 6 months
          <BaseIcon name="chevron-down" :size="16" />
        </button>
        <button class="tax-savings-card__more">
          <BaseIcon name="more" :size="18" />
        </button>
      </div>
    </div>

    <div class="tax-savings-card__value">
      <span class="tax-savings-card__amount">$11,756</span>
      <span class="tax-savings-card__change">
        <BaseIcon name="trending-up" :size="14" />
        12.75%
      </span>
    </div>

    <div class="tax-savings-card__chart">
      <div class="tax-savings-card__tooltip" v-if="selectedMonth === 'Mar'">
        <span class="tax-savings-card__tooltip-value">$5k</span>
      </div>
      <Line :data="chartData" :options="chartOptions" />
    </div>

    <div class="tax-savings-card__months">
      <button
        v-for="month in months"
        :key="month"
        :class="['tax-savings-card__month', { 'tax-savings-card__month--active': selectedMonth === month }]"
        @click="selectedMonth = month"
      >
        {{ month }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.tax-savings-card {
  background: white;
  border-radius: 12px;
  border: 1px solid #E5E7EB;
  padding: 1.5rem;
  height: 100%;
  display: flex;
  flex-direction: column;
}

.tax-savings-card__header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 0.5rem;
}

.tax-savings-card__title {
  font-size: 0.9375rem;
  font-weight: 500;
  color: #6B7280;
  margin: 0;
}

.tax-savings-card__actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.tax-savings-card__dropdown {
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

.tax-savings-card__dropdown:hover {
  background: #F9FAFB;
}

.tax-savings-card__more {
  display: flex;
  align-items: center;
  justify-content: center;
  background: none;
  border: none;
  color: #9CA3AF;
  cursor: pointer;
  padding: 0.25rem;
}

.tax-savings-card__more:hover {
  color: #6B7280;
}

.tax-savings-card__value {
  display: flex;
  align-items: baseline;
  gap: 0.75rem;
  margin-bottom: 1.5rem;
}

.tax-savings-card__amount {
  font-size: 1.75rem;
  font-weight: 700;
  color: #111827;
}

.tax-savings-card__change {
  display: flex;
  align-items: center;
  gap: 0.25rem;
  font-size: 0.875rem;
  font-weight: 500;
  color: #10B981;
}

.tax-savings-card__chart {
  position: relative;
  flex: 1;
  min-height: 180px;
  margin-bottom: 1rem;
}

.tax-savings-card__tooltip {
  position: absolute;
  top: 20%;
  left: 35%;
  background: #1F2937;
  color: white;
  padding: 0.375rem 0.625rem;
  border-radius: 6px;
  font-size: 0.8125rem;
  font-weight: 500;
  z-index: 10;
}

.tax-savings-card__tooltip::after {
  content: '';
  position: absolute;
  bottom: -4px;
  left: 50%;
  transform: translateX(-50%);
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: 5px solid #1F2937;
}

.tax-savings-card__months {
  display: flex;
  justify-content: space-between;
  gap: 0.25rem;
}

.tax-savings-card__month {
  flex: 1;
  background: none;
  border: none;
  padding: 0.5rem 0.25rem;
  font-size: 0.8125rem;
  color: #9CA3AF;
  cursor: pointer;
  border-radius: 6px;
  font-family: inherit;
  transition: all 0.15s ease;
}

.tax-savings-card__month:hover {
  color: #6B7280;
}

.tax-savings-card__month--active {
  background: #1F2937;
  color: white;
}
</style>
